import random

choice = 'y'
while choice == 'y' or choice == 'Y':
    try:
        n = int(input('How many random values I should generate? : '))
        propability = list()
        for i in range(n):
            propability.append(random.random())
        propability = sorted(propability)

        with open('percent.txt', 'w') as f:
            for i in propability:
                f.write(str(i) + ';{:.0%}'.format(round(i, 2)) + '\n')
    except ValueError:
        print('Only integers!')
    except NameError:
        print('Getting the number of random values failed!')
    choice = input('You want to try again? [Y/n]: ')