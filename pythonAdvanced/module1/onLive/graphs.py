#   my_list = []
#   for index in range(6):
#       my_list.append(index+1)

# list comprehension
my_list = [ index+1 for index in range(6) ]     # stwórz mi listę [ z operacją wykonywaną w for'ze o takim zakresie]
print(my_list)


#   my_list2 = []
#   for i in range(10):
#       my_list2.append(i*i)

# list comprehension
my_list2 = [ i*i for i in range(10) ]
print(my_list2)


#   my_list3 = []
#   for i in range(10):
#       if (i % 2 == 0):
#           my_list3.append(i*i)

# list comprehension + if
my_list3 = [ i*i for i in range(10) if i % 2 == 0 ]
print(my_list3)


#   my_list4 = []
#   for i in range(10):
#       if (i % 2 == 0):
#           my_list4.append(i*i)
#       else:
#           my_list4.append(0)

# list comprehension + if-else
my_list4 = [ i*i if i % 2 == 0 else 0 for i in range(10)]
print(my_list4)


# exercise_1:
#   my_list5 = []
#   for i in [8,10,15,19,25]
#       if i // 3 >= 5:
#           mu_list5.append(a+2)

# list comprehension exercise_1
my_list5 = [i+2 for i in [8, 10, 15, 19, 25] if i // 3 >= 5]
print(my_list5)


# exercise_2:
#   my_list6[]
#   for x in range(5, 21):
#       if x%2==1:
#           -x**2
#       else:
#           my_list6.append("HAHA")

my_list6 = [ -x**2 if x%2 == 1 else "HAHA" for x in range(5, 21) ]
print(my_list6)