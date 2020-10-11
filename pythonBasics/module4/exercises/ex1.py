names=["Beata", "Michal", "Norbert", "Grzegorz", "Justyna"]

with open("names.txt", "w") as f:
    for name in names:
        line = name + " " + str(len(name)) + "\n"
        f.write(line)
names_file = []
names_len = []

with open("names.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        name, n = line.split(",")
        names_file.append(name)
        n = int(n.strip())
        names_len.append(n)

print(names_file, names_len)