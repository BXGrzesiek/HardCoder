def fun1(x):
    i = 1
    for i in range(x + 1):
        print('*' * i)
        x = x - 1

def fun2(x):
#     j = 1
#     if j != x:
#         print('*' * j)
#         j = j + 1
#     else:
#         return x * fun2(x-1)


fun1(4)
print('\n')
fun2(6)