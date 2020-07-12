# The following program will always display only one of the answers.
# What one character can be added to the code to display another answer?
# (each of the variants can be achieved provided that one relevant character is added to the code).
# val = 10/3
# if val > 3:
#     print("big")
# elif val == 3:
#     print("middle")
# else:
#     print("small")
print('to get result \'big\'')
val = 10/3
if val > 3:
    print("big")
elif val == 3:
    print("middle")
else:
    print("small")

print('to get result \'middle\'')
val = 10//3
if val > 3:
    print("big")
elif val == 3:
    print("middle")
else:
    print("small")

print('to get result \'small\'')
val = -10/3
if val > 3:
    print("big")
elif val == 3:
    print("middle")
else:
    print("small")