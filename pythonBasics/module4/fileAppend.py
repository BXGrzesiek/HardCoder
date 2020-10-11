with open("demo.txt", "a") as f:
    f.write("\nJeszcze jedna linia")

with open("demo.txt", "r") as f:
    print(f.read())