# Write a function that takes a first name as an argument,
# then returns "female" or "man".
# Take advantage of some property
# of standard Polish names, which in the
# most will work here, ignore the exceptions.
# Then define an array with 5 different names
# friends and using the created function,
# create a dictionary that contains pairs name: gender.

def genderNameChecker(name):
    gender = ''
    if str(name[-1]) == 'a':
        gender = 'woman'
    else:
        gender = 'man'
    return gender

choice = 'Y'
while choice == 'Y' or choice == 'y':
    name = str(input('Your name: '))
    print(genderNameChecker(name))
    choice = input('You wanna try again? [Y/n]: ')