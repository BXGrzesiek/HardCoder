from math import pi

def circle(r):
    result = pi * pow(r, 2)
    return result

def triangle(a, h):
    result = 0.5 * a * h
    return result

def rectangle(a, b=1):
    result = a * b
    if b == 1 or b == a:
        choice = figures[3]
        print(str(choice))
    return result

def calculator(choice):
    if choice == 1:
        r = int(input('Provide r: '))
        print('Pole figury ' + figures[choice-1]
        + ' o podanych wartościach wynosi: ' + str(circle(r)))
    elif choice == 2:
        a = int(input('Provide a: '))
        h = int(input('Provide h: '))
        print('Pole figury ' + figures[choice-1]
        + ' o podanych wartościach wynosi: ' + str(triangle(a, h)))
    elif choice == 3:
        a = int(input('Provide a: '))
        b = int(input('Provide b: '))
        if a == b:
            print('Pole figury ' + figures[choice]
            + ' o podanych wartościach wynosi: ' + str(rectangle(a, b)))
        else:
            print('Pole figury ' + figures[choice-1]
            + ' o podanych wartościach wynosi: ' + str(rectangle(a, b)))

# script / program initiation
print('CALCULATOR v1.0\n\n\tOption list: ')
figures = ['circle', 'triangle', 'rectangle', 'square']

for figure in figures[:3]:
    print('\t' + str(figures.index(figure)+1) + ': ' + figure)

choice = int(input('Provide figure name [1|2|3]: '))
calculator(choice)