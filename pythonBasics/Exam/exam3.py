from os import system, name
from time import sleep


# -----------VARIABLES-------------- #

x = 0
shopping_list = []
ballance = 100.0
shopping_cart = ''
product_costs = dict()
choice = 'y'


# -----------FUNCTIONS-------------- #

def removeDuplicates(shopping_cart):
    for i in shopping_cart:
        if i not in shopping_list:
            shopping_list.append(i)


def addValues():
    for i in shopping_list:
        try:
            x = float(input('Cost for product: ' + i + ' is: '))
            if isinstance(x, (int, float)) and isPositive(x):
                product_costs.update({i.upper(): float(x)})
            else:
                print('Products can not be negative, the product: ' + i
                + ' will not be included in the cost estimate.')
                product_costs.update({i.upper(): 0})
        except ValueError:
            print('Wrong value - item: (' + i + ') expelled from Shopping List')
    print(product_costs)

def isEnough():
    bill = sum(list(product_costs.values()))
    if bill > ballance:
        print('You need more money (' + str(ballance-bill)
        + ') - It\'s not enough!')
    elif bill == ballance:
        print('You\'ve come to the estimation - that\'s exactly how much money you need')
    else:
        print('You have enough funds :)\nYour rest: ' + str(ballance-bill), end="\n")

def isPositive(x):
    if x >= 0:
        return True
    else:
        return False


# -----------BODY------------------- #

while choice =='y' or choice == 'Y':
    print('SHOPPING LIST - - Your declared account balance is: ' + str(ballance))
    shopping_cart = input('Provide shopping list as [apples,bananas,carrots,bread]: ')
    shopping_cart = shopping_cart.replace(' ', '').split(',')
    removeDuplicates(shopping_cart)
    shopping_list = sorted(shopping_list)
    addValues()
    isEnough()
    choice = input('Do you want to try again? [Y/n]: ')
    if choice == 'y' or choice == 'Y':
        print('Clearing the screen')
        sleep(3)
        print('\n'*30)
    else:
        break