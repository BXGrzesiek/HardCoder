#Write a simplified calculator that asks the user to enter
#two numbers and assigns their values to two variables x and y.
#Then displays their sum, difference, product and quotient.
#When calculating the quotient, add a condition to check that the second number is not 0!

print("Welcome to CALCULUS! Let's count something! :D"
+"\nPlease enter two numbers (variable values): ", end="")
X=input('X : ')
Y=input('Y : ')
try:
    val = float(X)
    val = float(Y)
except ValueError:
    print("Data Validation error - Float must be separated by a dot!")
    try:
        val=float(X)
        val=float(Y)
    except ValueError:
        print("No.. input is not a number. It's a string")

def function(X, Y):
    try:
        print("Addition Result: " + str(float(X)+float(Y)))
        print("Difference Result: " + str(abs(float(X)-float(Y))))
        print("Multiplication Result: " + str(float(X)*float(Y)))
        print("Division Result: " + str(float(X)/float(Y)))
    except ZeroDivisionError:
        print("Remember - never divide by zero!")

function(X, Y)