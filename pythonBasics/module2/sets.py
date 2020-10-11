#   sets - unordered items (no repetition)
#   syntax - - variableName = { item1, item2, item3 } - (!)curly braces(!)

#   an example :
my_set = { 1, 2, 3 }

#   the position of the added element is chosen randoly
my_set.add(5)

#   retrieve and return "the last" (random) element
my_set = { 1, 2, 3, 4, 1, 1, 1, 1, 1}
print(my_set)   #   {1, 2, 3, 4}

#pobranie i zwrócenie ostatniego elementu w zbiorze (losowo)
x=my_set.pop()
print(x)

#   is the element (5) in the set?
print(5 in my_set) # true | false
