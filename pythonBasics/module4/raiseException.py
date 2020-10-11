def square_area(a):
    if a <= 0:
        raise ValueError    # throm Exception manually if logical error, but correct for python
    return a*a

try:
    print(square_area(5))
    print(square_area(-5))
except ValueError:
    print("You don't know math?!")