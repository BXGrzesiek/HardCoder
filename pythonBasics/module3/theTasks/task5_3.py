def colors():
    return ["red", "green", "blue", "pink"]

def avg(tab):
    return sum(tab)/len(tab)

def get_number():
    a = input("Give me number:")
    return int(a)

def get_value1(aaa):
    print(aaa)

def get_value2(aaa):
    return aaa


tab = [1, 2, 3, 4, 5]
aaa = [1, 2, 3, 4, 5]
print(type(colors()))
print(type(avg(tab)))
print(type(get_number()))
print(type(get_value1(aaa)))
print(type(get_value2(aaa)))