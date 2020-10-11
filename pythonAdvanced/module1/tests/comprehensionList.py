#   2) Generate a list containing:
#   - negative squares of
#   - odd numbers 5 to 20
#   - and the string "haha" for
#   - even numbers in this range.

my_list = [-x**2 if x % 2 != 0 else "HAHA" for x in range(5, 21)]
print(my_list)