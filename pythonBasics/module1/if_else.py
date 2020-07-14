print("Interactive script")
repeat = 'Y'
while(repeat == 'Y' or repeat == 'y'):
    print("[1]\tComparison of the two numbers A and B: [1] ")
    print("[2]\tcheck user_age - can user play in Witcher game? ")
    print("[3]\tCheck result for y>10 and x<5 or z=100 ")
    choice = int(input('Provide 1 | 2 | 3 : '))
    if int(choice) == 1:
        print("Comparison of variables! \nProvide A: ", end="")
        a = input()
        print("Provide B: ", end="")
        b = input()
        if a == b:
            print("A = B")
        else:
            print("A is not equal to B")
    elif (int(choice) == 2):
        print("Can I play the witcher? \nLet's check, you only have one chance! \nPlease enter age: ", end="")
        age = input()
        if int(age) > 18:
            print("You can play Witcher!")
        elif int(age) == 18:
            print("Congratulations on having obtained your rights this year!")
        else:
            print("You can't play Witcher - yet :(")
    elif (int(choice) == 3):
        print("Boolean result for: \n|==> y>10 and x<5 or z=100 <==|")
        x = 4
        y = 5
        z = 50
        print('\t\t', end="")
        print(y > 10 and x < 5 or z == 100)
    else:
        print("Wrong answer!")
    rep = str(input("You want to repeat? [Y/n]"))
print('End of script!')