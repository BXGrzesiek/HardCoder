def compare(a,b,c):
    if a > b and b < c:
        return 3
    elif a < b and c == 3:
        return 5
    elif a <= b and c > 1:
        return 10
    else:
        return 99

print(compare(3,1,2) )
print(compare(3,2,1) )
print(compare(3,3,3) )
print(compare(1,2,3) )
print(compare(3,2,3) )
print(compare(1,1,1) )