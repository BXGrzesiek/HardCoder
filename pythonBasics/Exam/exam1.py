from math import pi


# -----------FUNCTIONS-------------- #

def circle(r):
    if r <= 0:
        return "Invalid Data\nDataValidationFailed - radius must be positive!\n\n"
    result = pi * pow(r, 2)
    return result

def triangle(a, h):
    if a <= 0 or h <= 0:
        return "Invalid Data\nDataValidationFailed - length must be positive!\n\n"
    result = 0.5 * a * h
    return result

def rectangle(a, b=1):
    if a <= 0 or b <= 0:
        return "Invalid Data\nDataValidationFailed - length must be positive!\n\n"
    result = a * b
    if b == 1 or b == a:
        choice = figures[3]
        print(str(choice))
    return result

def calculator(choice):
    if choice == 1:
        r = int(input('Provide r: '))
        print('Area of figure type:  \t' + figures[choice-1]
        + '\nwith the given values is: \t{:.2f}'.format(circle(r)))
    elif choice == 2:
        a = int(input('Provide a: '))
        h = int(input('Provide h: '))
        print('Area of figre type: \t' + figures[choice-1]
        + '\nwith the given values is: \t{:.2f}'.format(triangle(a, h)))
    elif choice == 3:
        a = int(input('Provide a: '))
        b = int(input('Provide b: '))
        if a == b:
            print('Area of figre type: \t' + figures[choice]
            + '\nwith the given values is: \t{:.2f}'.format(rectangle(a, b)))
        else:
            print('Area of figre type: \t' + figures[choice-1]
            + '\nwith the given values is: \t{:.2f}'.format(rectangle(a, b)))
    else:
        print('We are here \t--> nowhere ;) \n\t\t--> try again')


# -----------VARIABLES-------------- #

figures = ['circle', 'triangle', 'rectangle', 'square']
repeat = 'y'


# -----------BODY------------------- #

while repeat == 'y' or repeat == 'Y':
    try:
        print('CALCULATOR v1.0.2\n\n\tOption list: ')
        for figure in figures[:3]:
            print('\t' + str(figures.index(figure)+1) + ': ' + figure)
        choice = int(input('Provide figure name [1|2|3]: '))
        calculator(int(choice))
        repeat = input('You want to try again? [Y/n]')
    except ValueError:
        print('Value Error! \tPlease provide correct data!')
        repeat = input('You want to try again? [Y/n]')