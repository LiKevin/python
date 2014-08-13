__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
# list all those immutable types defined in Python; codes sourcing from 'copy.py'
########################################################################################################################


def _copy_immutable(x):
    return x

for t in (type(None), int, long, float, bool, str, tuple,
          frozenset, type, xrange, types.ClassType,
          types.BuiltinFunctionType, type(Ellipsis),
          types.FunctionType, weakref.ref):
    d[t] = _copy_immutable
for name in ("ComplexType", "UnicodeType", "CodeType"):
    t = getattr(types, name, None)
    if t is not None:
        d[t] = _copy_immutabl