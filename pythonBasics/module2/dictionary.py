my_dict={"apples" : 5, "bananas": 10}
print(my_dict)

#   create shopping list
#   print it and display costs

shopping = {"tomatoes" : 3,
            "carrots" : 2,
            "onions"    : 4,
            "paprika"   : 12}
print(shopping)
print(shopping.items())
print(sum(shopping.values()))

#   dictionary update mode
my_dict.update( {3: "trzy"})
my_dict[4] = "cztery"

#   deleting element
del my_dict[4]