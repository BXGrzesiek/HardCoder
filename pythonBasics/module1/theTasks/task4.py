#Write a program that calculates a rectangular trapezoid field with bases 4 and 9 and arms 12 and 13.
print("Calculation The rectangular trapezoidal area.")
A=4
B=9
C=12
D=13
print("Given dimensions of the figure: "
+ "\nbase A: " + str(A)
+ "\nbase B: " + str(B)
+ "\narm1: \t" + str(C)
+ "\narm2: \t" + str(D)
+ "\nheight could be C or D. We have to check that.")
print("For rectangular trapeze, we know that the height will be the shortest arm. "
+ "\nThe IF conditional statement selects the appropriate value: ")

if C>D:
    H=D
    print("\nThe height is equal with D: " + str(D))
elif C==D:
    H=C=D
    print("\nBoth arms are the same?! How is that possible? Wrong data??")
else:
    H=C
    print("\nThe height is qual with C: " + str(C))

result=((A+B)*H)/2
print("\nThe area of the rectangular trapezoid is: ", end="")
print(int(result))
print("Figure circumference: ", end="")
print(A+B+C+D)
