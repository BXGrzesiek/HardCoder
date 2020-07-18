# Using the function and if-elif-else conditions, write a simplified calculator,
# which will perform an operation on two numbers specified by the user.
# The calculator asks the participant for the action they want to perform via the input () function,
# and then after reading the given character (e.g. :
# "+" - adding,
# "-" - adding,
# "*" - multiplication,
# "/" - addition) prompts you to enter the numbers a and b.
# Then it calls the appropriate function.
# Keep security in mind if the user wants to enter incorrect values.
# You can use isnumeric () - find out how it works.

def addition(a=1, b=1):
    return a+b
def difference(a=1, b=1):
    return a-b
def multiplication(a=1, b=1):
    return a*b
def division(a=1, b=1):
    return a/b
def calculator(A, B):
    try:
        option = input('Choose option [+|-|*|/]: ')
        if option == "+":
            print('You chosed mode Addition: ')
            print("Addition Result: " + str(addition(int(A), int(B))))
        elif option == "-":
            print('You chosed mode difference')
            print("Difference Result: " + str(difference(int(A), int(B))))
        elif option == "*":
            print('You chosed mode Multiplication')
            print("Multiplication Result: " + str(multiplication(int(A), int(B))))
        elif option == "/":
            print('You chosed mode Division')
            print("Division Result: " + str(division(int(A), int(B))))
        else:
            print('Wrong Value!')
    except ZeroDivisionError:
        print("Remember - never divide by zero!")
    except ValueError:
        print("Data Validation error - Float must be seperated by a dot!")

print("Welcome to CALCULUS! Let's count something! :D")
choice = 'Y'
while choice == 'Y' or choice == 'y':
    print('# “+” - addition, \n# “-” - difference, \n# “*” - multiplication, \n# “/” - division)')
    print("Please enter two numbers (variable values): ")
    A = input("|> A: ")
    B = input("|> B: ")
    calculator(A, B)
    print('You want to try again?')
    choice = str(input('[Y/n]'))