# Ask the user about AGE and amount of MONEY in the wallet.
# Then check whether the user can buy alcohol worth PLN 20 in the store.
# Consider all 4 cases, only one of which meets the condition
# "you meet the age requirements and you have enough cash!".
# Display the relevant information for each case
#   AGE     MONEY
#    0        0
#    1        0
#    0        1
#    1        1

def function():
    choice = 'T'
    while choice == 'T' or choice == 't':
        print("\nPlease enter two informations your age and cash balance: ")
        X = int(input("|> Age: "))
        Y = float(input("|> Money: "))

        if (int(X) >= 18 and float(Y) >= 20):
            print('you meet the age requirements and you have enough cash!')
        elif int(X) < 18 and float(Y) >= 20:
            print('you don\'t meet the age requirements but you have enough cash!')
        elif int(X) >= 18 and float(Y) < 20:
            print('you meet age requirements but you don\'t have enough cash!')
        else:
            print('you don\'t meet the age requirements and you don\'t have enough cash!')

        choice = input('You wanna repeat? [T/n]')

print("Welcome to PURCHASE VALIDATOR! Let's check something! :D")
function()