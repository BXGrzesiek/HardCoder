#with open("demo.txt", "r") as my_file:
    # operation1
    # operation2
    # operation3
# in this case - po wyjściu z bloku automatycznie zamyka się plik

# with open("demo.txt", "r") as f:
#     content = f.read()
#     print(content)
#     # all works

# here not
# print(f)

# nadpisanie pliku - kasuje zawartość
# with open("demo.txt", "w") as f:
#     pass

with open("demo.txt", "w") as f:
    f.write("To jest pierwsza\n")
    f.write("To jest druga linia")
    # brak \n i linie sie skleją
    f.write("To jest trzecia linia")

with open("demo.txt", "r") as f:
    print(f.read())