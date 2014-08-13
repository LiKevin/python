# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
# fixme: list all those leagal types predefined in python2.7
# fixme:  generate new objects by using the type(); with which to call the constructor per defined(e.g: list, set, dict)
########################################################################################################################

# demo 1
########################################################################################################################
import types

for type in dir(types):
    print type

del type

# outputs: all leagal types defined by Python "types" module
########################################################################################################################
#BooleanType
#BufferType
#BuiltinFunctionType
#BuiltinMethodType
#ClassType
#CodeType
#ComplexType
#DictProxyType
#DictType
#DictionaryType
#EllipsisType
#FileType
#FloatType
#FrameType
#FunctionType
#GeneratorType
#GetSetDescriptorType
#InstanceType
#IntType
#LambdaType
#ListType
#LongType
#MemberDescriptorType
#MethodType
#ModuleType
#NoneType
#NotImplementedType
#ObjectType
#SliceType
#StringType
#StringTypes
#TracebackType
#TupleType
#TypeType
#UnboundMethodType
#UnicodeType
#XRangeType


# demo 2:  do the copy by invoking the constructor from the type(); useful for list/ set/ dict
########################################################################################################################
a = ['a', 'b', 'c']
print type(a)('b')      # fixme:  create new list by invoking the type constructor
