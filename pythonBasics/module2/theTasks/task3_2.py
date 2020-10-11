from collections import *

x1 = 1234
x2 = [1, 2, 3, 4]
x3 = {1, 2, 3, 4}
x4 = {1: 2, 3: 4}
x5 = (1 , 2 , 3, 4)
x6 = 1, 2, 3, 4

# print(x1 + 'is mutable ' + str(isinstance(x1, MutableSequence)))
# print(x2 + 'is mutable ' + str(isinstance(x2, MutableSequence)))
# print(x3 + 'is mutable ' + str(isinstance(x3, MutableSequence)))
# print(x4 + 'is mutable ' + str(isinstance(x4, MutableSequence)))
# print(x5 + 'is mutable ' + str(isinstance(x5, MutableSequence)))
# print(x6 + 'is mutable ' + str(isinstance(x6, MutableSequence)))


type1 = type(x1)
type2 = type(x2)
type3 = type(x3)
type4 = type(x4)
type5 = type(x5)
type6 = type(x6)

print(isinstance(type1, MutableSequence))
print(str(type1) + 'is mutable ' + str(isinstance(type1, MutableSequence)))
print(str(type2) + 'is mutable ' + str(isinstance(type2, MutableSequence)))
print(str(type3) + 'is mutable ' + str(isinstance(type3, MutableSequence)))
print(str(type4) + 'is mutable ' + str(isinstance(type4, MutableSequence)))
print(str(type5) + 'is mutable ' + str(isinstance(type5, MutableSequence)))
print(str(type6) + 'is mutable ' + str(isinstance(type6, MutableSequence)))

# def is_mutable(cls):
#     return hasattr(cls, '__setitem__')

# typeTab = [x1, x2, x3, x4, x5, x6]
# for type_ in typeTab:
#     print(type_, 'is mutable?: ', is_mutable(type_))