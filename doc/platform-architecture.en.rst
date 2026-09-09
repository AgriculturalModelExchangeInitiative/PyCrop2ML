Transformation Platform Architecture
=====================================

Motivation for the Refactor
----------------------------

PyCropML performs two families of transformations:

* a **source platform** converts a component from an external framework
  (APSIM, BioMA, Python, etc.) into a Crop2ML package;
* a **target platform** converts a Crop2ML package into code, or into a
  package consumable by a target language or framework (Python, OpenAlea,
  Java, C#, etc.).

Historically, ``cyml.py`` had direct knowledge of the modules, classes,
file paths and idiosyncrasies of every platform. This produced tight
coupling: onboarding a new platform could require touching several places
deep in PyCropML's core.

The current architecture separates these concerns through platform
contracts, registries, a facade, a pipeline, and a generation context.

Overview
--------

The control flow for a transformation *into* a target looks like this::

    User or CLI
         |
         v
    cyml.transpile_package()          public facade
         |
         v
    TargetPipeline                    orchestration
         |
         +----> target_registry ----> TargetPlatform
         |
         +----> GenerationContext
         |
         +----> ModelUnit generator
         +----> composition generator
         +----> optional hooks

The flow for a transformation *from* a source platform is more direct::

    cyml.transpile_component()
         |
         v
    source_registry ----> SourcePlatform.convert()
                              |
                              v
                         Crop2ML package

Design by Contract
-------------------

**Design by contract** means stating explicitly what a component must
provide, and what the rest of the system is entitled to expect from it.
Calling code depends on the contract, never on a concrete implementation.

In this architecture, the public contracts are:

``SourcePlatform``
    Describes an ingestion platform and exposes a single ``convert``
    operation. The contract guarantees that any registered source knows
    how to turn an external component into Crop2ML.

``TargetPlatform``
    Describes a target: its name, Python module, ModelUnit generator,
    composer, file extensions, and optional capabilities. The pipeline
    consumes this contract without ever importing a Python, OpenAlea or
    Java generator directly.

``GenerationContext``
    Defines the information made available to every generation step:
    models, composition, component name, working directories, metadata
    and options.

This is a **contract-first design**: the types, required fields and
public methods *are* the contract. It is not yet a formal implementation
of *Design by Contract* with preconditions, postconditions and invariants
enforced by a dedicated framework — though a handful of preconditions are
already checked, such as rejecting a ``TargetPlatform`` whose name or
module is empty.

The contracts buy the following guarantees:

* the CLI can tell a source apart from a target;
* every built-in platform speaks the same interface;
* the core no longer depends on any single concrete implementation;
* optional capabilities are declared explicitly rather than inferred;
* future third-party platforms can adopt the identical contract.

The Facade Pattern
-------------------

A **Facade** provides a small, stable interface in front of a larger,
more intricate subsystem. It hides the sequencing of internal operations
and shrinks the surface area the caller needs to know about.

The ``pycropml.cyml`` module plays this role. Its functions remain the
public entry points:

* ``transpile_file(source, language)``;
* ``transpile_package(package, language)``;
* ``transpile_component(component, package, language)``.

Callers keep writing::

    from pycropml.cyml import transpile_package

    transpile_package("energybalance_pkg", "py")

without ever having to instantiate the registry, the topology, the
context or the pipeline themselves. For package generation, the facade
now simply delegates to::

    TargetPipeline(package, language).run()

This indirection lets the internal implementation evolve freely without
breaking the API surface relied on by the CLI, notebooks and downstream
client code.

The Registry Pattern
----------------------

A **registry** maps a stable identifier to an object descriptor or a
factory. It replaces scattered ``if/elif`` chains and becomes the single
source of truth for which platforms are available.

``source_registry.py``
    Maps a name such as ``apsim`` or ``bioma`` to a ``SourcePlatform``.

``target_registry.py``
    Maps a name such as ``py`` or ``openalea`` to a ``TargetPlatform``.

Resolution is conceptually::

    name supplied by the CLI
             |
             v
    get_source(name) or get_target(name)
             |
             v
    platform contract

Concrete classes and functions are resolved through **lazy loading** via
``importlib``: a given dependency is only imported once the matching
platform is actually requested.

The Pipeline Pattern
----------------------

A **Pipeline** structures a transformation as an ordered sequence of
stages, each one consuming the results or context produced by the stage
before it.

``TargetPipeline`` now owns the orchestration logic that used to live
inside ``cyml.transpile_package``. Its execution order is:

#. resolve and validate the requested ``TargetPlatform``;
#. parse the Crop2ML XML files into ModelUnit objects;
#. create the output directories;
#. generate the intermediate CyML models;
#. build the composition topology;
#. populate the ``GenerationContext``;
#. invoke the domain-class and wrapper hooks;
#. transform each ModelUnit into the target language;
#. generate the composition's algorithm and code;
#. invoke the optional simulation hook.

This ordering is load-bearing and must be preserved: for instance,
transforming ModelUnits reads the CyML files produced earlier, and
generating hooks depends on the composition built by ``Topology``.

The pipeline owns the **when** and the **in what order**. The
``TargetPlatform`` owns the **what to load or call**. The concrete
generators retain ownership of the **how code gets produced**.

The Generation Context
------------------------

``GenerationContext`` is a **Context Object**: it bundles the data needed
across several operations so that no plugin has to accept its own long,
bespoke argument list.

Its fields represent:

``package``
    Root path of the Crop2ML package being processed.

``package_name``
    The package's name as it appears on the filesystem.

``target_name``
    Identifier of the target resolved from the registry.

``model_units``
    ModelUnit objects built from the XML descriptions.

``composition``
    The composite model produced by ``Topology``.

``component_name``
    Name of the composition or of the top-level component.

``crop2ml_directory``
    Directory holding the Crop2ML XML descriptions.

``cyml_directory``
    Directory of intermediate CyML/``pyx`` algorithms.

``target_root``
    Root directory of the target, e.g. ``src/py``.

``target_package``
    Directory of the generated package, e.g.
    ``src/py/energybalance_pkg``.

``test_directory``
    Directory for target-specific tests.

``documentation_directory`` and ``image_directory``
    Directories for generated documentation and diagrams.

``metadata``
    Open-ended dictionary for additional descriptive information.

``options``
    Open-ended dictionary for per-run options.

Both dictionaries make small extensions possible without immediately
touching the context's constructor. That said, any piece of data that is
fundamental and shared across every platform should graduate to an
explicit field rather than stay an implicit key buried in ``options``.

Hooks
-----

A **hook** is an extension point the core invokes only when a platform
declares the matching capability. It lets behavior be added without
threading a platform-specific branch through the pipeline.

The current target hooks are:

``domain_class_factory``
    Produces the domain classes required by certain platforms.

``wrapper_factory``
    Produces an adapter, or wrapper, around the composition.

``simulation_class``
    Produces the files needed to run a simulation. Currently used only
    by the Python target.

``generate_notebooks``
    Signals that test notebooks should be produced for the ModelUnits.

A missing hook simply means an unsupported capability, not an error: the
pipeline skips that optional step and moves on.

Compatibility with Legacy Generators
--------------------------------------

Older hooks were not yet written to accept a ``GenerationContext``
directly. ``TargetPlatform`` temporarily plays the role of an **adapter**
between the new pipeline and these legacy signatures.

Conceptually, the pipeline calls::

    target.generate_wrapper(context)

and ``TargetPlatform`` translates that call into the existing signature::

    wrapper_factory(
        context.composition,
        context.target_package,
        context.component_name,
    )

This is a textbook application of the **Adapter pattern**: a new
interface is translated into an existing one, sparing every generator an
immediate rewrite. Over time, new hooks will be able to consume the
context directly, once a compatibility and versioning policy has been
defined.

Division of Responsibilities
-------------------------------

=============================== =============================================
Component                       Responsibility
=============================== =============================================
``cyml.py``                     Public facade invoked by the CLI and by
                                user code.
``SourcePlatform``              Contract for a conversion into Crop2ML.
``TargetPlatform``              Contract and capabilities of a target.
``source_registry.py``          Catalog and resolution of sources.
``target_registry.py``          Catalog and resolution of targets.
``TargetPipeline``              Ordered orchestration of a target
                                generation run.
``GenerationContext``           Data shared across steps and hooks.
``Main``                        Parses and transforms a ModelUnit's
                                algorithm into the target language.
``Topology``                    Reads and translates the composition.
Concrete generators              Produce platform-specific code.
=============================== =============================================

Adding a Built-in Platform
-----------------------------

Under the current architecture, integrating a new platform into PyCropML
itself follows these steps:

#. implement its source converter or target generators in a dedicated
   module;
#. register a ``SourcePlatform`` or ``TargetPlatform`` in the matching
   registry;
#. declare only the optional capabilities that are genuinely supported;
#. add tests covering lazy loading and contract compliance;
#. add at least one representative end-to-end transformation test.

Conceptual example of a target declaration::

    TargetPlatform(
        name="my_platform",
        module="pycropml.transpiler.generators.my_platform",
        generator="ModelUnitGenerator",
        composer="CompositionGenerator",
        extension="py",
        composition_extension="xml",
        wrapper_factory="generate_wrapper",
        generate_notebooks=True,
    )

The pipeline itself needs no changes as long as the platform stays
within the bounds of the existing contract. A genuinely new
cross-cutting capability must first be defined in the contract,
documented, and only then orchestrated by the pipeline.

A target whose ModelUnits and composition share the same output format
only needs to declare ``extension``:
``effective_composition_extension`` then falls back to it automatically.
A mixed platform — Python Steps alongside an XML Workflow, say — declares
both separately::

    TargetPlatform(
        ...,
        extension="py",
        composition_extension="xml",
    )

The composer returns the generated content; ``TargetPipeline`` retains
sole responsibility for the output path and for writing the file with
the correct extension.

External Target Platforms
----------------------------

A target can now be distributed as an independent, installable Python
package. The third-party package publishes its contract through a
Python **entry point** declared in its ``pyproject.toml``::

    [project.entry-points."pycropml.targets"]
    my_platform = "my_plugin.platform:target"

The ``target`` object exposed by ``my_plugin.platform`` can be a
``TargetPlatform`` instance directly::

    from pycropml.transpiler.target import TargetPlatform

    target = TargetPlatform(
        name="my_platform",
        module="my_plugin.generator",
        generator="ModelUnitGenerator",
        composer="CompositionGenerator",
        extension="py",
        api_version="1",
    )

Architectural view of the plugin extension point::

    PyCropML core (``pycropml`` package)            Installed third-party distribution
    -------------------------------------           --------------------------------------
    cyml.transpile_package()
           |
           v
    TargetPipeline.run()
           |
           v
    target_registry.get_target(name)
           |
           +--> TARGETS (built-in dict)
           |
           +--> discover_targets()
                      |
                      | importlib.metadata.entry_points(
                      |     group="pycropml.targets")
                      |
                      |        <-- package boundary -->
                      v
                 entry point "my_platform"
                      |
                      v
                 my_plugin.platform:target -----> TargetPlatform(...)
                                                          |
                                                          v
                                                   my_plugin.generator
                                                     .ModelUnitGenerator
                                                     .CompositionGenerator

The core never has prior knowledge of ``my_plugin``: ``discover_targets()``
only queries the ``pycropml.targets`` entry-point group exposed by the
running Python environment (every installed package, not PyCropML alone),
builds a ``TargetPlatform`` from whatever it finds, and the pipeline then
handles that object exactly like any built-in target — neither
``TargetPipeline`` nor ``target.py`` contains a single plugin-specific
branch. The only coupling between the two worlds is the contract itself and
its version (``api_version``): as long as the plugin honors ``TargetPlatform``
and the expected API version, the core can load, invoke, and evolve any
third-party target independently.

The entry point may instead expose a zero-argument factory that returns
this object. Once the third-party package is installed,
``available_targets()`` merges built-in and discovered targets alike, so
the new target shows up in the CLI's help output and can be used exactly
like any other::

    cyml -p energybalance_pkg my_platform

The entry point's name must match ``TargetPlatform.name`` exactly.
Built-in platform names are reserved, and two plugins may not publish
the same name: a collision raises an explicit error instead of silently
shadowing an existing platform.

Contract Versioning
----------------------

``TARGET_PLATFORM_API_VERSION`` states which contract version PyCropML
understands. Every ``TargetPlatform`` carries an ``api_version`` field,
currently ``"1"``. A platform declaring a different version is rejected
with a clear error message.

This version number describes the interface *between* PyCropML and the
platform — not the plugin's own functional version, which the plugin
tracks independently in its own ``pyproject.toml``. The API number should
only change alongside a backward-incompatible change to the contract
itself.

Current Limitation
---------------------

External discovery is currently available for target platforms only.
Source platforms already implement the ``SourcePlatform`` contract, but
discovering external sources through a ``pycropml.sources`` entry-point
group remains a separate, upcoming piece of work.

Maintenance Principles
-------------------------

To preserve this separation of concerns:

* never import a platform's generator directly inside ``cyml.py``;
* never add an ``if target == ...`` branch to the pipeline when the
  behavior can instead be expressed as a capability or a hook;
* route generation-time information exclusively through
  ``GenerationContext``;
* keep ``transpile_package`` a stable, backward-compatible API;
* load optional dependencies lazily, only when the matching platform is
  actually invoked;
* test the contract, the orchestration, and a real generation run as
  three separate concerns.
