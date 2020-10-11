#napisy (string)

string "ciąg znaków" pewne operacje wykonuje się analogicznie jak w listach/tuplach,
napisy są niemodyfikowalne [
name = "HardCoder"
#indexowanie
print(name[1])
#podzbiory
print( name[1:4])
#pozycja el
print( name.find("rd"))
#pozycja elementu nieistniejącego
print( name.find("X"))
#zmiana znaków
print( name.replace("Coder", "Word")
#zmiana wielkości liter
print( name.upper(), name.lower())
#podział względem znaku
print( "ty,ja,on".split(","))
#łączenie napisów z list
print("".join(["a","b","c"]))