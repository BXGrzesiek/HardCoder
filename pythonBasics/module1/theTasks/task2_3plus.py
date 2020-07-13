# The% (modulo) operator is also used for calculations, which calculates the remainder of the division.
# Example: 5 % 3 -> 2 (because 5/3 = 1 r 2).
# Ask the user for the number, and then check if the number is even or odd.
# PLUS - What if user will provide

def function():
    choice = 'T'
    while choice == 'T' or choice == 't':
        try:
            print("\nPlease enter number (variable value): ")
            X = int(input("|> X: "))
            if isinstance(X, int):
                print('Is an int!')
                if(int(X) % 2) == 0:
                    print("The number is even")
                else:
                    print("The number is odd")
            else:
                print('I can check only integer value!')
        except ZeroDivisionError:
            print("Remember - never divide by zero!")
        except ValueError:
            print('Is not integer!')
            pass

        print('\n\nYou want to try again? ', end="")
        choice = input('[Y/n] ')

print("Welcome to PARITY CHECKER! Let's check something! :D")
function()