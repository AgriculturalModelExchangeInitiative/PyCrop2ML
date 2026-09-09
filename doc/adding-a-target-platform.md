# Adding a Crop2ML Target Platform

This is a hands-on, step-by-step guide for writing a new **target platform**
for PyCropML — a plugin that turns a Crop2ML package into code for a
framework PyCropML doesn't ship with. It complements
[`platform-architecture.rst`](platform-architecture.rst): that document
explains the *why* (contracts, registry, pipeline, facade); this one walks
through the *how*, file by file.

The worked example throughout is a real, working plugin:
[`pycropml-ecrops`](https://github.com/AgriculturalModelExchangeInitiative/pycropml-ecrops)
— a target that turns Crop2ML ModelUnits into eCrops `Step` classes and
Crop2ML compositions into eCrops Workflow XML. Every command below has
actually been run against it; the output shown is real, not illustrative.

If you only need to add a platform *inside* the PyCropML source tree itself
(not as a separate installable package), the same steps apply minus the
packaging parts (steps 2 and 8) — you add your generator module directly
under `src/pycropml/transpiler/generators/` and register it in
`target_registry.py`'s `TARGETS` dict instead of via an entry point.

## Who this is for

You're building this if you can answer "yes" to: *"I have a target language
or framework, and I want `cyml -p mypackage mytarget` to produce code for
it."* You do **not** need to modify anything inside PyCropML itself — the
whole point of the contract described in `platform-architecture.rst` is that
your plugin is a self-contained, independently versioned Python package.

## Step 0 — Decide the shape of your target before writing code

Answer these questions first; they determine what you'll implement:

* **What does one Crop2ML ModelUnit become in your target?** A class? A
  function? A file? (For eCrops: an `ecrops.Step` subclass.)
* **What does a Crop2ML composition become?** Another block of the same
  target language, or a different artifact entirely (a config file, a
  workflow description, a graph)? (For eCrops: an XML Workflow, not Python —
  this is exactly why `TargetPlatform` has *two* extension fields, see
  Step 3.)
* **Does wiring between ModelUnits need extra generated code**, beyond what
  the ModelUnit generator and the composition generator produce on their
  own? (For eCrops: yes — a `wrapper_factory` hook generates small "Link
  Step" adapter classes that copy values between differently-named ports.
  See Step 6.)

Writing these down first avoids a common trap: reaching for a hook to solve
a problem that a slightly different design in your own generator would have
avoided. The pipeline calls hooks unconditionally when declared, so keep
them for genuinely cross-cutting concerns, not as a dumping ground.

## Step 1 — Read the contracts your plugin must satisfy

Two files define everything the pipeline expects from you. Read them before
writing anything:

* `src/pycropml/transpiler/target.py` — the `TargetPlatform` dataclass:
  every field it accepts, and `__post_init__`'s validation (a target with an
  empty name or module, or a mismatched `api_version`, is rejected at
  construction time, not at first use).
* `src/pycropml/transpiler/generation_context.py` — the `GenerationContext`
  dataclass your generator's methods will receive.

You do not need to read `target_pipeline.py` in detail to get started, but
knowing its execution order (documented in `platform-architecture.rst`) will
help you understand *when* each of your generator's methods gets called.

## Step 2 — Scaffold the package

A target plugin is an ordinary installable Python package. `pycropml-ecrops`
looks like this:

```text
pycropml-ecrops/
├── pyproject.toml
├── README.md
├── src/
│   └── pycropml_ecrops/
│       ├── __init__.py
│       ├── platform.py      # the TargetPlatform declaration
│       └── generator.py      # EcropsGenerator + EcropsComposer + hooks
└── tests/
    ├── test_platform.py       # contract compliance
    ├── test_generator.py      # unit-level generation
    └── test_integration.py    # end-to-end against a real Crop2ML package
```

Its `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "pycropml-ecrops"
version = "0.1.0"
description = "External PyCropML target platform for generating eCrops Steps"
readme = "README.md"
requires-python = ">=3.8,<3.13"
dependencies = ["pycropml"]

[project.optional-dependencies]
test = ["pytest"]
runtime = ["ecrops"]

[project.entry-points."pycropml.targets"]
ecrops = "pycropml_ecrops.platform:target"

[tool.setuptools.packages.find]
where = ["src"]
```

Two things worth copying exactly:

* `dependencies = ["pycropml"]` — your plugin depends on PyCropML, never the
  other way around.
* the `runtime` extra separates *generation-time* dependencies (just
  `pycropml`) from *execution-time* dependencies (the target framework
  itself, `ecrops` here). PyCropML never needs `ecrops` installed to
  generate eCrops code — only someone who wants to *run* the generated
  Workflow does.

## Step 3 — Declare the `TargetPlatform` contract

This is the smallest, most important file in the plugin — the one the core
actually touches:

```python
# src/pycropml_ecrops/platform.py
"""PyCropML target-platform declaration discovered through entry points."""

from pycropml.transpiler.target import TargetPlatform


target = TargetPlatform(
    name="ecrops",
    module="pycropml_ecrops.generator",
    generator="EcropsGenerator",
    composer="EcropsComposer",
    extension="py",
    composition_extension="xml",
    api_version="1",
    wrapper_factory="generate_link_steps",
)
```

Field by field:

* `name` — what users type after `cyml -p package`; must match the entry
  point name exactly (Step 7 enforces this at discovery time).
* `module` — where `generator`, `composer`, and every optional hook name are
  looked up *by string*, lazily, via `importlib`. Nothing in PyCropML
  imports `pycropml_ecrops` until this target is actually requested.
* `generator` / `composer` — the two classes you'll write in Step 4 and 5.
  Only their *names* live here; `TargetPlatform.load_generator()` /
  `load_composer()` resolve them on demand.
* `extension` / `composition_extension` — this is exactly the "mixed
  platform" case flagged in `platform-architecture.rst`: ModelUnits become
  `.py` files, but the composition becomes `.xml`. If your target used the
  same format for both, you'd omit `composition_extension` entirely and
  `effective_composition_extension` would fall back to `extension`.
* `api_version="1"` — must equal `TARGET_PLATFORM_API_VERSION` in
  `target.py` at the time you write the plugin. If PyCropML ever ships a
  version 2, an old plugin declaring `"1"` fails fast with a clear error
  instead of generating subtly wrong code against a changed contract.
* `wrapper_factory="generate_link_steps"` — an optional hook; see Step 6.
  Omit any hook field you don't need — a missing hook is a "not supported"
  capability, not an error (`TargetPlatform.generate_wrapper` is a no-op
  when `wrapper_factory` is `None`).

`__init__.py` just re-exports `target` so the entry point (Step 7) has
something short to point at:

```python
# src/pycropml_ecrops/__init__.py
from .platform import target

__all__ = ["target"]
```

## Step 4 — Implement the ModelUnit generator

This is the class named by `generator` in Step 3. Its job: turn *one*
Crop2ML ModelUnit's algorithm into your target language. You are not
starting from a blank AST walker — subclass one of PyCropML's existing
language generators and reuse its expression/statement translation, then
layer your framework's wrapper on top.

`EcropsGenerator` subclasses `PythonGenerator` (eCrops Steps *are* plain
Python) and appends a wrapper class after the translated algorithm body:

```python
class EcropsGenerator(PythonGenerator):
    """Render the algorithm as Python and expose it through ecrops.Step."""

    def visit_module(self, node):
        super().visit_module(node)                       # translate the algorithm
        self.result.append("\n\n" + self.render_step_class(node))
```

`render_step_class` then generates, from `self.model` (the `ModelUnit`
object PyCropML already parsed from the Crop2ML XML — you never parse XML
yourself), a small `Step` subclass exposing:

* `getparameterslist()` / `getinputslist()` / `getoutputslist()` — metadata
  dictionaries built from each variable's `description`, `datatype`,
  `unit`, category (parameter / input / state / rate / output), built by
  walking `self.model.parameters`, `self.model.inputs`, `self.model.outputs`;
* `setparameters(status)` — reads eCrops' shared `status.allparameters`,
  falling back to the Crop2ML `default=` attribute when one is declared;
* `initialize(status)` — calls the ModelUnit's own `init_*` function when
  the algorithm declares one (found by scanning the translated AST for a
  `function_definition` node whose name starts with `init_` — see
  `_find_function`);
* `runstep(status)` — calls the translated `model_*` function (the name
  `pycropml.render_cyml.signature()` gives the algorithm) with each
  argument read from — and each result written back into — a per-ModelUnit
  namespace on the shared `status` object (`_section` decides
  `parameters` / `inputs` / `states` / `rates` / `outputs` from each
  variable's Crop2ML category).

None of this is Crop2ML-specific plumbing you have to reinvent: `self.model`
already gives you fully-typed `Input`/`Output`/`Parameter` objects with
`.name`, `.datatype`, `.unit`, `.description`, `.variablecategory` /
`.parametercategory`, and `.default`. Mapping *those* fields onto your
target's own metadata format is the actual work.

## Step 5 — Implement the composition generator

Named by `composer` in Step 3, this class turns the *composition* — the
graph of linked ModelUnits — into your target's representation of a
workflow. Unlike the ModelUnit generator, it does not have to subclass an
existing language generator if your target's composition format isn't code
at all:

```python
class EcropsComposer(CodeGenerator):
    """Generate an eCrops Workflow XML from a Crop2ML composition."""

    def __init__(self, tree, model=None, name=None):
        super().__init__()
        self.tree = tree
        self.model = model     # the composition, not a single ModelUnit
        self.name = name

    def visit_module(self, node):
        self.write(self.build_workflow())
```

`self.model` here is the composition object: `.model` (the list of linked
ModelUnits), `.inputlink` / `.internallink` / `.outputlink` (the wiring),
`.inputs` / `.outputs` (the composition's own external ports). `build_workflow`
walks these to emit an ordered list of `<Step>` elements — one per
ModelUnit, in dependency order (`_stable_execution_order` performs a stable
topological sort over `internallink`, so ModelUnits that don't depend on
each other keep their declared order — reproducible output matters for
diffable generated code and for tests).

## Step 6 — Add an optional hook, if wiring needs its own generated code

`wrapper_factory` — like `domain_class_factory` and `simulation_class` — is
called unconditionally by the pipeline *when declared*, right after model
parsing and before per-ModelUnit generation (see the hook step in
`platform-architecture.rst`'s pipeline order). Its signature is fixed by
`TargetPlatform.generate_wrapper`:

```python
def generate_link_steps(composition, target_package, component_name):
    ...
```

eCrops needs this because a composition can link an output port to an
input port with a *different name* on the receiving ModelUnit — something
neither the ModelUnit generator (which only sees one ModelUnit) nor the
composition generator (which only emits `<Step>` references, not variable
assignments) can express alone. `generate_link_steps` writes one small
adapter `Step` class per ModelUnit that has incoming links, and the
composer inserts a `<Step>` reference to it *before* the ModelUnit's own
step in the Workflow.

If your target doesn't need this kind of adapter code, skip the hook
entirely rather than declaring one that does nothing — an absent hook is
free; a hook that's a no-op is not.

## Step 7 — Register the entry point

Already shown in Step 2's `pyproject.toml`:

```toml
[project.entry-points."pycropml.targets"]
ecrops = "pycropml_ecrops.platform:target"
```

The entry-point **name** (`ecrops`, left of `=`) must equal
`TargetPlatform.name` (also `"ecrops"`) exactly —
`target_registry._load_external_target` checks this and raises a clear
`ValueError` at discovery time if they ever drift apart. Built-in target
names are reserved, and two installed plugins cannot register the same
name; either collision fails loudly instead of one plugin silently
shadowing the other.

## Step 8 — Install and confirm discovery

```bash
conda activate crop2ml
python -m pip install -e /path/to/PyCropML          # if not already installed
cd pycropml-ecrops
python -m pip install -e .
```

Confirm PyCropML actually sees it — no PyCropML code changes, no restart of
anything beyond the Python process itself:

```bash
$ cyml --help
...
Available targets: r, cs, cpp, cpp2, py, f90, java, simplace, sirius,
openalea, check, apsim, record, dssat, stics, bioma, ecrops
```

`ecrops` is there, merged in among the built-in targets, exactly as
`platform-architecture.rst`'s extension diagram describes: `cyml`'s core
never had `pycropml_ecrops` hard-coded anywhere — `discover_targets()` found
it by querying the `pycropml.targets` entry-point group of the current
Python environment.

## Step 9 — Test at three levels

`pycropml-ecrops`'s own test suite is a good template — three genuinely
different things are worth checking separately:

**Contract compliance** (`test_platform.py`) — does the declaration itself
satisfy what `TargetPlatform` promises, with no Crop2ML input at all?

```python
def test_entry_point_exposes_versioned_ecrops_target():
    assert isinstance(target, TargetPlatform)
    assert target.name == "ecrops"
    assert target.api_version == "1"
    assert target.extension == "py"
    assert target.composition_extension == "xml"
    assert target.effective_composition_extension == "xml"
    assert target.load_generator().__name__ == "EcropsGenerator"
    assert target.load_composer().__name__ == "EcropsComposer"
    assert target.wrapper_factory == "generate_link_steps"
```

**Unit-level generation** (`test_generator.py`) — does your generator
produce the right output for a hand-built or minimal ModelUnit, without
going through the full pipeline?

**End-to-end integration** (`test_integration.py`) — does a *real* Crop2ML
package, run through the actual `transpile_package()` facade, produce
output that is at minimum syntactically valid and structurally correct?
`pycropml-ecrops` runs this against PyCropML's own `example/Monica_SoilTemp`
fixture:

```python
transpile_package(package, "ecrops")

generated = package / "src" / "ecrops" / "Monica_SoilTemp"
python_files = sorted(generated.glob("*.py"))
assert len(python_files) == 6
for path in python_files:
    compile(path.read_text(encoding="utf-8"), str(path), "exec")
```

— compiling every generated file is a cheap, high-value check: it catches
the entire class of "produced text that merely *looks* like the target
language" bugs before anyone tries to run the output for real.

## Step 10 — Run it for real

This was actually executed against a scratch copy of
`example/Monica_SoilTemp` while writing this guide:

```bash
$ cyml -p Monica_SoilTemp ecrops
Monica_SoilTemp/doc/images/SoilTemperatureComp.png

$ find Monica_SoilTemp/src/ecrops -type f | sort
Monica_SoilTemp/src/ecrops/Monica_SoilTemp/SoilTemperatureCompComponent.xml
Monica_SoilTemp/src/ecrops/Monica_SoilTemp/link_inputs_to_no_snow_soil_surface_temperature.py
Monica_SoilTemp/src/ecrops/Monica_SoilTemp/link_inputs_to_soil_temperature.py
Monica_SoilTemp/src/ecrops/Monica_SoilTemp/link_inputs_to_with_snow_soil_surface_temperature.py
Monica_SoilTemp/src/ecrops/Monica_SoilTemp/nosnowsoilsurfacetemperature.py
Monica_SoilTemp/src/ecrops/Monica_SoilTemp/soiltemperature.py
Monica_SoilTemp/src/ecrops/Monica_SoilTemp/withsnowsoilsurfacetemperature.py
```

Three ModelUnits (`NoSnowSoilSurfaceTemperature`, `WithSnowSoilSurfaceTemperature`,
`SoilTemperature`) each got their own `.py` file; two of them additionally
got a `link_inputs_to_*.py` adapter because they receive links from a
sibling ModelUnit; the composition became one Workflow XML. A fragment of
the generated `soiltemperature.py`, confirmed to `compile()` cleanly:

```python
    def runstep(self, status):
        model = self._model(status)
        model.states.soilTemperature = model_soiltemperature(
            model.parameters.noOfSoilLayers, ...,
            model.states.soilSurfaceTemperature, ...,
        )
        return status
```

## Recap: the mapping table is the real design artifact

Every non-trivial target plugin ends up needing one table like this
(`pycropml-ecrops`'s `README.md` documents exactly this one) — write it
*before* you write `generator.py`, not after:

| Crop2ML concept | Target representation |
| --- | --- |
| ModelUnit | Python `Step` class |
| Composition | Workflow XML |
| Composition input | Driving variable or parameter |
| InputLink | Assignment in a generated Link Step |
| InternalLink | Assignment in a generated Link Step |
| Composition output | Workflow output variable |
| ModelUnit dependency | Workflow Step order |

Everything in Steps 4–6 is really just this table, implemented.

## Where to go from here

* `platform-architecture.rst` — the conceptual model behind everything
  above (contracts, registry, pipeline, facade, adapter), and the current
  limitation that external *source* platforms (converting an existing
  framework component *into* Crop2ML) don't yet have the same entry-point
  discovery that targets do — only `SourcePlatform`'s static in-tree
  registry exists today.
* the built-in generators under `src/pycropml/transpiler/generators/` —
  `pythonGenerator.py`, `csharpGenerator.py`, `javaGenerator.py`, and others
  are all real subclassing examples of exactly the pattern in Step 4, for
  languages PyCropML already ships.
