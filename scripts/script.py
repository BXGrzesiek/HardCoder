from time import sleep


coffe_cups = 3
bugs_reported = 0
bugs_fixed = 0


scriptError = input('BUG reported? [Y/n] ')
while scriptError == 'Y':
    bugs_reported += 1
    print('Keep Going - no break - more coffee - customer is waiting :)')
    coffe_cups += 1
    print('Cups of coffee today - ' + str(coffe_cups))
    sleep(60)
    fixed = (input('Fixed? [Y/n] '))
    if fixed == 'Y':
        bugs_fixed += 1
    else:
        print('It\'s not a BUG it\'s a Feature :D')
    print('Bugs Fixed' + str(bugs_fixed))
    scriptError = input('New BUG reported? [Y/n] ')