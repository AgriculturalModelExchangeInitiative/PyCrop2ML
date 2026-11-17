# The Odin target

```bash
cyml -p Monica_SoilTemp odin
```

generates an [Odin](https://odin-lang.org) package in
`Monica_SoilTemp/src/odin/Monica_SoilTemp/`. Its structure follows the `cpp2`
target, so the generated code can be called from a host model the same way.

## Generated API

For a composition `SoilTemperatureComp` in package `Monica_SoilTemp`
(`package monica_soiltemp`):

| File | Contents |
| --- | --- |
| `SoilTemperatureCompState.odin` (and `Rate`, `Auxiliary`, `Exogenous`) | `Soil_Temperature_Comp_State :: struct {...}`, `destroy_soil_temperature_comp_state` |
| `SoilTemperature.odin`, one per ModelUnit | `Soil_Temperature :: struct {...}` with the ModelUnit's parameters, `make_soil_temperature` (parameter defaults), `destroy_soil_temperature`, `soil_temperature_init`, `soil_temperature_calculate_model` |
| `SoilTemperatureCompComponent.odin` | `Soil_Temperature_Comp_Component :: struct {...}` holding the ModelUnits, `make_`/`destroy_`, one `..._set_<parameter>` per composition parameter, `..._init`, `..._calculate_model` |

All `init` and `calculate_model` procs take the same arguments: the ModelUnit
(or Component), then pointers to the State, the previous-day State (`s1`), the
Rate, Auxiliary and Exogenous structs. They read and write those structs in
place.

```odin
c := monica_soiltemp.make_soil_temperature_comp_component()
defer monica_soiltemp.destroy_soil_temperature_comp_component(&c)
s, s1: monica_soiltemp.Soil_Temperature_Comp_State
// ... r, a, ex; free with the destroy_* procs
monica_soiltemp.soil_temperature_comp_component_set_layer_thickness(&c, layer_thickness[:])
monica_soiltemp.soil_temperature_comp_component_init(&c, &s, &s1, &r, &a, &ex)
for day in days {
	ex.tmin, ex.tmax, ex.globrad = ...
	monica_soiltemp.soil_temperature_comp_component_calculate_model(&c, &s, &s1, &r, &a, &ex)
}
```

## Translation rules

* Names: variables and procs become `snake_case`, types `Ada_Case`
  (`noOfSoilLayers` → `no_of_soil_layers`). Odin keywords and builtins get a
  trailing `_`. If two Crop2ML names would become the same Odin name (`V` and
  `v`), generation fails with an error naming both.
* Types: `DOUBLE` → `f64`, `INT` → `int`, `BOOLEAN` → `bool`, `STRING`/`DATE` →
  `string`, arrays and lists → `[dynamic]T`.
* Odin has no implicit numeric conversion: an `int` operand of a floating-point
  operation is wrapped in `f64(...)`. Integer literals stay untyped constants.
* `log(x)` → `math.ln(x)`, `log(x, base)` → `math.log(x, base)`.
* Transcendental functions can go through MONICA's `support/cr_math` (CORE-MATH, correctly
  rounded) instead of `core:math`: set `CYML_ODIN_MATH` to its import path *as seen from the
  generated package*, e.g.

  ```bash
  CYML_ODIN_MATH=../../support/cr_math cyml -p Monica_SoilTemp odin
  ```

  `exp`, `log`/`ln`, `pow`, `sin`, `cos`, `tan`, `asin`, `acos` and `atan` then use `cr_math`
  (`log(x, base)` becomes `cr_math.log(x) / cr_math.log(base)`); `sqrt`, `floor`, `ceil`,
  `round`, `is_nan`, `sum` and `PI` stay `core:math`. Executables then link `cr_math_lib`.
* Helper functions of a ModelUnit are `@(private="file")`, so equal names in
  different ModelUnits don't collide. They take arrays as slices and return lists
  and arrays as slices.

## Memory

* Each struct owns its dynamic arrays; free them with its `destroy_*` proc.
* `init` sizes arrays with `resize`, so calling it twice does not leak.
* Local arrays in procs are freed with `defer delete(...)` unless they are
  returned. A caller copies list/array results of a helper into its own arrays
  and frees the result if the helper allocated it.
* Procs that may allocate (`make_*`, `*_init`, `*_calculate_model`, the Component's list/array
  setters) take `allocator := context.allocator` as their last parameter and make it the
  context allocator for everything they call, so a host can pass e.g. an arena.

## Checking the output

```bash
odin check src/odin/Monica_SoilTemp -no-entry-point -vet
```

`test/cyml/test_odin_generator.py` runs this check when an Odin compiler is on
`PATH` or in `$ODIN`, and skips it otherwise.
