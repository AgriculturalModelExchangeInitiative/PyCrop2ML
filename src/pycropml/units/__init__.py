from unyt import UnitRegistry, Unit, array
import unyt
from unyt import *
from unyt import unit_object
from numbers import Number as numeric_type
from types import MethodType
import numpy as np
from unyt.array import _coerce_iterable_units,_preserve_units,_comparison_unit
from unyt.array import _get_binary_op_return_class,_arctan2_unit,_multiply_units, _divide_units
from unyt.exceptions import (
    InvalidUnitOperation,
    MissingMKSCurrent,
    MKSCGSConversionError,
    UnitConversionError,
    UnitsNotReducible,
     UnitOperationError,
     InvalidUnitEquivalence,
    UnitParseError,
    IterableUnitCoercionError
)
from unyt.dimensions import (
    angle,
    base_dimensions,
    dimensionless,
    temperature,
    current_mks,
    #logarithmic
)

from numpy import (
    add,
    subtract,
    multiply,
    divide,
    logaddexp,
    logaddexp2,
    true_divide,
    floor_divide,
    negative,
    power,
    remainder,
    mod,
    absolute,
    rint,
    sign,
    conj,
    exp,
    exp2,
    log,
    log2,
    log10,
    expm1,
    log1p,
    sqrt,
    square,
    reciprocal,
    sin,
    cos,
    tan,
    arcsin,
    arccos,
    arctan,
    arctan2,
    hypot,
    sinh,
    cosh,
    tanh,
    arcsinh,
    arccosh,
    arctanh,
    deg2rad,
    rad2deg,
    bitwise_and,
    bitwise_or,
    bitwise_xor,
    invert,
    left_shift,
    right_shift,
    greater,
    greater_equal,
    less,
    less_equal,
    not_equal,
    equal,
    logical_and,
    logical_or,
    logical_xor,
    logical_not,
    maximum,
    minimum,
    fmax,
    fmin,
    isreal,
    iscomplex,
    isfinite,
    isinf,
    isnan,
    signbit,
    copysign,
    nextafter,
    modf,
    ldexp,
    frexp,
    fmod,
    floor,
    ceil,
    trunc,
    fabs,
    spacing,
    divmod as divmod_,
    isnat,
    ones_like,
    matmul
)
trigonometric_operators = (sin, cos, tan)
POWER_SIGN_MAPPING = {multiply: 1, divide: -1}

class _ImportCache(object):
    
    __slots__ = ["_ua", "_uq"]

    def __init__(self):
        self._ua = None
        self._uq = None

    @property
    def ua(self):
        if self._ua is None:
            from unyt.array import unyt_array

            self._ua = unyt_array
        return self._ua

    @property
    def uq(self):
        if self._uq is None:
            from unyt.array import unyt_quantity

            self._uq = unyt_quantity
        return self._uq

_import_cache_singleton = _ImportCache()

def mult(self, u):
    """ Multiply Unit with u (Unit object). """
    if not getattr(u, "is_Unit", False):
        data = np.array(u, subok=True)
        unit = getattr(u, "units", None)
        if unit is not None:
            if self.dimensions is logarithmic:
                raise InvalidUnitOperation(
                    "Tried to multiply '%s' and '%s'." % (self, unit)
                )
            units = unit * self
        else:
            units = self
        if data.dtype.kind not in ("f", "u", "i", "c"):
            raise InvalidUnitOperation(
                "Tried to multiply a Unit object with '%s' (type %s). "
                "This behavior is undefined." % (u, type(u))
            )
        if data.shape == ():
            return _import_cache_singleton.uq(data, units, bypass_validation=True)
        return _import_cache_singleton.ua(data, units, bypass_validation=True)
    elif self.dimensions is logarithmic and not u.is_dimensionless:
        raise InvalidUnitOperation("Tried to multiply '%s' and '%s'." % (self, u))
    elif u.dimensions is logarithmic and not self.is_dimensionless:
        raise InvalidUnitOperation("Tried to multiply '%s' and '%s'." % (self, u))

    base_offset = 0.0
    if self.base_offset or u.base_offset:
        if u.dimensions in (temperature, angle) and self.is_dimensionless:
            base_offset = u.base_offset
        elif self.dimensions in (temperature, angle) and u.is_dimensionless:
            base_offset = self.base_offset
        else:
            raise InvalidUnitOperation(
                "Quantities with dimensions of angle or units of "
                "Fahrenheit or Celsius cannot be multiplied."
            )
    return Unit(
        self.expr * u.expr,
        base_value=(self.base_value * u.base_value),
        base_offset=base_offset,
        dimensions=(self.dimensions * u.dimensions),
        registry=self.registry,
    )

#unit.__class__=type('Unit',(Unit,),{'__mul__':mult})

#unyt.unit_object.Unit = unit
def truediv(self, u):
    """ Divide Unit by u (Unit object). """
    if not isinstance(u, Unit):
        if isinstance(u, (numeric_type, list, tuple, np.ndarray)):
            from unyt.array import unyt_quantity

            return unyt_quantity(1.0, self) / u
        else:
            raise InvalidUnitOperation(
                "Tried to divide a Unit object by '%s' (type %s). This "
                "behavior is undefined." % (u, type(u))
            )

    base_offset = 0.0
    if self.base_offset or u.base_offset:
        if self.dimensions in (temperature, angle) and u.is_dimensionless:
            base_offset = self.base_offset
        '''else:
            raise InvalidUnitOperation(
                "Quantities with units of Farhenheit "
                "and Celsius cannot be divided."
            )'''

    return Unit(
        self.expr / u.expr,
        base_value=(self.base_value / u.base_value),
        base_offset=base_offset,
        dimensions=(self.dimensions / u.dimensions),
        registry=self.registry,
    )



def array_ufunc(self, ufunc, method, *inputs, **kwargs):
    func = getattr(ufunc, method)
    if "out" not in kwargs:
        out = None
        out_func = None
    else:
        # we need to get both the actual "out" object and a view onto it
        # in case we need to do in-place operations
        out = kwargs.pop("out")[0]
        if out.dtype.kind in ("u", "i"):
            new_dtype = "f" + str(out.dtype.itemsize)
            float_values = out.astype(new_dtype)
            out.dtype = new_dtype
            np.copyto(out, float_values)
        out_func = out.view(np.ndarray)
    if len(inputs) == 1:
        # Unary ufuncs
        inp = inputs[0]
        u = getattr(inp, "units", None)
        if u.dimensions is angle and ufunc in trigonometric_operators:
            # ensure np.sin(90*degrees) works as expected
            inp = inp.in_units("radian").v
        # evaluate the ufunc
        out_arr = func(np.asarray(inp), out=out_func, **kwargs)
        if ufunc in (multiply, divide) and method == "reduce":
            # a reduction of a multiply or divide corresponds to
            # a repeated product which we implement as an exponent
            mul = 1
            power_sign = POWER_SIGN_MAPPING[ufunc]
            if "axis" in kwargs and kwargs["axis"] is not None:
                unit = u ** (power_sign * inp.shape[kwargs["axis"]])
            else:
                unit = u ** (power_sign * inp.size)
        else:
            # get unit of result
            mul, unit = self._ufunc_registry[ufunc](u)
        # use type(self) here so we can support user-defined
        # subclasses of unyt_array
        ret_class = type(self)
    elif len(inputs) == 2:
        # binary ufuncs
        i0 = inputs[0]
        i1 = inputs[1]
        # coerce inputs to be ndarrays if they aren't already
        inp0 = _coerce_iterable_units(i0)
        inp1 = _coerce_iterable_units(i1)
        u0 = getattr(i0, "units", None) or getattr(inp0, "units", None)
        u1 = getattr(i1, "units", None) or getattr(inp1, "units", None)
        ret_class = _get_binary_op_return_class(type(i0), type(i1))
        if u0 is None:
            u0 = Unit(registry=getattr(u1, "registry", None))
        if u1 is None and ufunc is not power:
            u1 = Unit(registry=getattr(u0, "registry", None))
        elif ufunc is power:
            u1 = inp1
            if inp0.shape != () and inp1.shape != ():
                raise UnitOperationError(ufunc, u0, u1)
            if isinstance(u1, unyt_array):
                if u1.units.is_dimensionless:
                    pass
                else:
                    raise UnitOperationError(ufunc, u0, u1)
            if u1.shape == ():
                u1 = float(u1)
            else:
                u1 = 1.0
        unit_operator = self._ufunc_registry[ufunc]
        if unit_operator in (_preserve_units, _comparison_unit, _arctan2_unit):
            # check "is" equality first for speed
            if u0 is not u1 and u0 != u1:
                # we allow adding, multiplying, comparisons with
                # zero-filled arrays, lists, etc or scalar zero. We
                # do not allow zero-filled unyt_array instances for
                # performance reasons. If we did allow it, every
                # binary operation would need to scan over all the
                # elements of both arrays to check for arrays filled
                # with zeros
                if not isinstance(i0, unyt_array) or not isinstance(i1, unyt_array):
                    any_nonzero = [np.count_nonzero(
                        i0), np.count_nonzero(i1)]
                    if any_nonzero[0] == 0:
                        u0 = u1
                    elif any_nonzero[1] == 0:
                        u1 = u0
                if not u0.same_dimensions_as(u1):
                    if unit_operator is _comparison_unit:
                        # we allow comparisons between data with
                        # units and dimensionless data
                        if u0.is_dimensionless:
                            u0 = u1
                        elif u1.is_dimensionless:
                            u1 = u0
                        else:
                            raise UnitOperationError(ufunc, u0, u1)
                    else:
                        raise UnitOperationError(ufunc, u0, u1)
                conv, offset = u1.get_conversion_factor(u0, inp1.dtype)
                new_dtype = np.dtype("f" + str(inp1.dtype.itemsize))
                conv = new_dtype.type(conv)
                '''if offset is not None:
                    raise InvalidUnitOperation(
                        "Quantities with units of Fahrenheit or Celsius "
                        "cannot by multiplied, divided, subtracted or "
                        "added with data that has different units."
                    )'''
                inp1 = np.asarray(inp1) * conv
        # get the unit of the result
        mul, unit = unit_operator(u0, u1)
        # actually evaluate the ufunc
        out_arr = func(
            inp0.view(np.ndarray), inp1.view(np.ndarray), out=out_func, **kwargs
        )
        if unit_operator in (_multiply_units, _divide_units):
            if unit.is_dimensionless and unit.base_value != 1.0:
                if not u0.is_dimensionless:
                    if u0.dimensions == u1.dimensions:
                        out_arr = np.multiply(
                            out_arr.view(np.ndarray), unit.base_value, out=out_func
                        )
                        unit = Unit(registry=unit.registry)
            '''if (
                u0.base_offset
                and u0.dimensions is temperature
                or u1.base_offset
                and u1.dimensions is temperature
            ):
                print(u0.base_offset,u0.dimensions,u1.base_offset,u1.dimensions)
                raise InvalidUnitOperation(
                    "Quantities with units of Fahrenheit or Celsius TODO "
                    "cannot by multiplied, divide, subtracted or added."
                )'''
    else:
        raise RuntimeError(
            "Support for the %s ufunc with %i inputs has not been"
            "added to unyt_array." % (str(ufunc), len(inputs))
        )
    if unit is None:
        out_arr = np.array(out_arr, copy=False)
    elif ufunc in (modf, divmod_):
        out_arr = tuple((ret_class(o, unit) for o in out_arr))
    elif out_arr.size == 1:
        out_arr = unyt_quantity(np.asarray(out_arr), unit)
    else:
        if ret_class is unyt_quantity:
            # This happens if you do ndarray * unyt_quantity.
            # Explicitly casting to unyt_array avoids creating a
            # unyt_quantity with size > 1
            out_arr = unyt_array(out_arr, unit)
        else:
            out_arr = ret_class(out_arr, unit, bypass_validation=True)
    if out is not None:
        if mul != 1:
            multiply(out, mul, out=out)
            if np.shares_memory(out_arr, out):
                mul = 1
        if isinstance(out, unyt_array):
            try:
                out.units = out_arr.units
            except AttributeError:
                # out_arr is an ndarray
                out.units = Unit("", registry=self.units.registry)
    if mul == 1:
        return out_arr
    return mul * out_arr


def uappend(self, val):
    import numpy as np
    return unyt_array(np.append(self.value, val), self.units)

    
array.unyt_array.__array_ufunc__=array_ufunc
array.unyt_array.append=uappend
Unit.__mul__=mult
Unit.__truediv__=truediv


def Int(self):
    print(self.units)
    if isinstance(self, unyt_quantity):
        return unyt_quantity(int(self.value), self.units)


#array.unyt_array.__int__=Int

cyml_reg = UnitRegistry('mks')

class Simulation(object):
    def __init__(self, registry):
        self.registry = registry
    def array(self, value, units):
        return unyt.unyt_array(value, units, registry=self.registry)
    def quantity(self, value, units):
        return unyt.unyt_quantity(value, units, registry=self.registry)

# dimensionless
dimless = {"plants":"plants", "leaf":"leaf"}


def reg_():
    if "mmW" not in cyml_reg:
        cyml_reg.add("mmW", base_value=1.0, dimensions=unyt.dimensions.mass/unyt.dimensions.area, tex_repr=r"\rm{mm water}")
    if "j" not in cyml_reg:
        cyml_reg.add("j", base_value=1.0, dimensions=unyt.dimensions.energy, tex_repr=r"\rm{joule}")
    if "C_degC" not in cyml_reg:
        cyml_reg.add("C_degC", base_value=1.0, offset=273.15, dimensions=unyt.dimensions.temperature, tex_repr=r"\rm{joule}")
    for k in dimless.keys():
        if k not in cyml_reg:
            cyml_reg.add(k, base_value=1.0, dimensions=unyt.dimensions.dimensionless, tex_repr=r"\rm{v}")     
    return cyml_reg

rg = reg_()
cyml_units = Simulation(rg)

from unyt.unit_systems import add_symbols
class UnitContainer(object):
    def __init__(self, registry):
        add_symbols(vars(self), registry)
    
u = UnitContainer(cyml_units.registry)

def Cint(v):
    return int(v)*v.units

def Cfloat(v):
    return float(v)*v.units

