# string+int wrong type exception
# dzielenie przez 0
# błedna rzutowanie int("text")
# wyjście poza zakres tablicy
# nieistniejący plik (błędna ścieżka)

# try-except
# try:
    # operacja mogąca wykonać błąd
# except nazwaSpodziewanegoWyjątku:
    # operacje do wykonania jak się błąd pojawi
# ZeroDivisionError
for i in range(-2,2):
    try:
        print(10/i)
    except ZeroDivisionError:
        print("Ej przez zero się nie dzieli")

# FileNotFoundError
try:
    with open("new_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Plik nie istnieje i nie mógł zostać otarty!")

# dont use:
# except:
    # print("Dowolny inny błąd")
