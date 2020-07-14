# variables - boxes for datas
#    print("Put your name here: ")
#    user_name=input()
#    print("How old are you? ")
#    user_age=input()
#    print("Hi, " + user_name + "(" + user_age + ")")
# keyword list
#    import keyword
#    print(keyword.kwlist)

print("Interactive script - CALCULUS")
repeat = 'Y'
while(repeat == 'Y' or repeat == 'y'):
    print("[1]\tCalculate the trapezoid area: ")
    choice = int(input('Provide 1 : '))
    if int(choice) == 1:
        print("Program for counting the trapezoid field.\nBase length A: ")
        a = input()
        print("Base length B: ")
        b = input()
        print("Height: ")
        h = input()
        print("Result of AREA=(H*(A+B))/2 is: ")
        print(((int(a)+int(b))*int(h))/2)
    # elif (int(choice) == 2):

    else:
        print("Wrong answer!")
    rep = str(input("You want to repeat? [Y/n]"))
print('End of script!')