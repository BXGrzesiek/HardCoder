#Write a program that in two different ways causes
#the result of dividing the numbers 100 and 33 will be 3
#(without a fractional part).
a=100
b=33
stWay=a/b
ndWay=a//b
print("Result of dividing numbers 100 per 33 - in two ways.\n")
print("1'st way - variable typecasting to integer")
print("\tresult: ", end="")
print(int(stWay), end="\n\n")
print("2'nd way - using operator \"//\": ")
print("\tresult: ", end="")
print(ndWay)