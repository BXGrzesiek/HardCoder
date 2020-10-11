#game

for y in range(5):
    for x in range(6):
        if ((x==0 and y==1)
            or (x==2 and y==3)
            or (x==2 and y==4)
            or (x==3 and y==4)):
            print("x", end="")
        elif ((x==1 and y==1)
            or (x==2 and y==0)
            or (x==3 and y==3)
            or (x==5 and y==3)): # obsługa monet
            print("*", end="")
        elif (y==2):
            print("=", end="")
        else:
            print(".", end="")
    print()     #po przejściu x'ów - nowa linia
# print("Another Way\n\n")
# points=[[".",".","*",".",".","."],
#         ["x","*",".",".",".","."],
#         ["=","=","=","=","=","="],
#         [".",".","x","*",".","*"],
#         [".",".","x","x",".","."]]
#print(points)
# for y in range(points[y]):
#     for x in range(points[x]):
#         print(points[x][y])
#print()