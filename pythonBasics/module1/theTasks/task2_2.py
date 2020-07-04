#Write a simplified calculator that asks the user to enter
#two numbers and assigns their values to two variables x and y.
#Then displays their sum, difference, product and quotient.
#When calculating the quotient, add a condition to check that the second number is not 0!


def function():
    choice = 'T'
    while choice=='T' or choice=='t':
        try:
            print("\nPlease enter two numbers (variable values): ")
            X= input("|> X: ")
            #X= float(X)
            Y= input("|> Y: ")
            #Y= float(Y)
            print("Addition Result: " + str(float(X)+float(Y)))
            print("Difference Result: " + str(abs(float(X)-float(Y))))
            print("Multiplication Result: " + str(float(X)*float(Y)))
            print("Division Result: " + str(float(X)/float(Y)))
        except ZeroDivisionError:
            print("Remember - never divide by zero!")
        except ValueError:
            print("Data Validation error - Float must be seperated by a dot!")
        print('You want to try again?')
        choice=input(str)

print("Welcome to CALCULUS! Let's count something! :D")
function()