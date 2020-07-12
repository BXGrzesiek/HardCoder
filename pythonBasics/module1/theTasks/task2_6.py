#     Write a simple tax calculator for income tax.
#     First, the program will ask the user if
#     he wants to provide monthly or annual income.
#     If you choose monthly income, calculate the annual income.
#
#     Then, based on the values provided,
#     calculate the value of the annual income tax
#     based on the I and II tax threshold (17% and 32%)
#     - you can find the tax calculation method
#     according to tax thresholds on the Internet.

def taxes(income):
    if float(income) > 85528:
        rest = float(income) - 85528
        print('Your income has exceeded the 2\'nd tax threshold: ${:.2f}'.format(rest))
        first = 85828*0.17
        second = float(rest)*0.32
        summary = (float(first)+(float(second)))
        print('Amount to pay according to 1\'st tax threshold: ${:.2f}'.format(first))
        print('Amount to pay according to 2\'nd tax threshold: ${:.2f}'.format(second))
        print('The sum to be paid against taxes: ${:.2f}'.format(summary))
    else:
        print('Your income has not exceeded the first tax threshold')
        print('\n- you\'ll pay less (normmally)! :)\n')
        summary = float(income)*0.17
        print('The sum to be paid against taxes: ${:.2f}'.format(summary))

def function():
    choice = 'T'
    while choice == 'T' or choice == 't':
        print('Please choose mode: \n1) monthly income \n2) annual income')
        mode = input('[1] or [2]: ')

        if (int(mode) == 1):
            print('Mode \"1 - monthly income\" is active!"')
            print('\nPlease provide monthly income')
            income = input('Income month: $')
            income = float(income)*12
            print('Got it!\tYour yearly income is: ${:.2f}'.format(income))
            taxes(income)

        else:
            print('Mode \"2 - annual income\" is active!')
            print('\nPlease provide annual income')
            income = float(input('Income per year: $'))
            # income = float(income)
            print('Got it!\t Your yearly income is: ${:.2f}'.format(income))
            taxes(income)
        choice = input('You want to repeat? [T/n]: ')

print('Welcome to TAX Calculator!')
print('\nI\'m sorry I have to count how much $.$ the government will take!')
function()