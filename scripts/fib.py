#   script generating a list with fibonacci sequence elements
#   the user is asked for the number of elements
#   to reduce the load of computing power,
#   the list is displayed after all X elements have been generated

from time import sleep


def fib(n):
    try:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 2)+fib(n - 1)
    except ValueError:
         print('Only positive integer!')


choice = 'y'
while choice == 'y' or choice == 'Y':
    print('Series of Fibonacci numbers')
    print('\n'*5)
    n = int(input('How deep you want to go? : '))
    print(type(n))
    elements = []
    for i in range(n):
        elements.append(fib(i))
    print(elements)
    choice = input('You want to try again? [Y/n] ')
    if choice == 'y' or choice == 'Y':
        print('Clearing the screen')
        sleep(3)
        print('\n'*30)
    else:
        break