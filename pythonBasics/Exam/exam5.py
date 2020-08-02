import datetime
import time
choice = 'y'
while choice == 'y' or choice == 'Y':
    try:
        n = int(input('how long should I collect logs? [s]: '))
        with open('logs.txt', 'w') as f:
            for i in range(n):
                time.sleep(1)
                f.write(str(i)
                + '|'
                + str(datetime.date.today().day)
                + ' '
                + str(datetime.date.today().month)
                + ' '
                + str(datetime.date.today().year)
                + '|'
                + str(datetime.datetime.today().hour)
                + ':'
                + str(datetime.datetime.today().minute)
                + ':'
                + str(datetime.datetime.today().second)
                + '|'
                + str(datetime.datetime.today().timestamp)
                + '\n')
    except ValueError:
        print('Only integers!')
    except NameError:
        print('Getting the number of seconds failed!')
    choice = input('You want to try again? [Y/n]: ')