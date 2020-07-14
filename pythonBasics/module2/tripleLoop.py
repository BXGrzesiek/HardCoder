# How loop nesting works

print("List of coordinates.")
for x in range(10):
    for y in range(10):
        for z in range(5):
            print("\nPiksel: "
            + str(x)
            + ","
            + str(y)
            + ","
            + str(z), end="")
            if (int(x) == 1 and int(y) == 2 and int(z) == 3):
                print(" ==> Enemy!")
            elif (x == 6 and y == 5 and z == 4):
                print(" ==> Enemy!")
            elif (x == 7 and y == 8 and z == 0):
                print(" ==> Enemy!")
            elif (x == 9 and y == 7 and z == 1):
                print(" ==> Friend!")
            else:
                continue