num = input("Give me number:")
try:
    num = float(num)
except ValueError:
    num = 0
finally:
    print(num*num)