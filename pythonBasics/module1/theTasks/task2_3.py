#The% (modulo) operator is also used for calculations, which calculates the remainder of the division.
#Example: 5 % 3 -> 2 (because 5/3 = 1 r 2).
#Ask the user for the number, and then check if the number is even.

def function():
    choice = 'T'
    while choice=='T' or choice=='t':
        try:
            print("\nPlease enter number (variable value): ")
            X= input("|> X: ")
            if(int(X)%2)==0:
                print("The number is even")
            else:
                print("The number is odd")
        except ZeroDivisionError:
            print("Remember - never divide by zero!")
        except ValueError:
            print("Data Validation error - Float must be seperated by a dot!")
        print('\n\nYou want to try again?')
        choice=input(str)

print("Welcome to PARITY CHECKER! Let's check something! :D")
function()