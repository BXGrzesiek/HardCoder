# try-except-finally


try:
    for i in range(-2,2):
        print(10/i)
except ZeroDivisionError:
    print("Ej przez zero się nie dzieli")
finally:
    print("Koniec!")