def fun1(x):
    i=1
    for i in range(x+1):
        print('*'*i)
        x=x-1

def fun2(x):
    i=1
    if i==x:
        print('*'*i)
        x=x-1

x=0
fun(4)