# -----------VARIABLES-------------- #
repeat = 0
numbers = list()
choice = 'y'

# -----------FUNCTIONS-------------- #
def listing(numbers):
    for number in numbers:
        print(number)


# -----------BODY------------------- #
while choice == 'y' or choice == 'Y':
    try:
        repeat = input('Provide number: ')  # type string
        if repeat == 'exit':
            listing(numbers)
            break
        else:
            numbers.append(float(repeat))
    except ValueError:
        print('You provide ' + str(len(numbers)) + ' numbers. I don\'t want to play anymore!')
        break