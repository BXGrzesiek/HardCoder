

def calculus():
    a = float(input('Provide A: '))
    b = float(input('Provide B: '))
  # c = float(input('Provide C: '))
    h = float(input('Provide H: '))
    return a, b, h

def figureTrapezoid(a, b, h):
    return (a+b)*h/2

def figureTriangle(a, h):
    return (a*h)/2
# need to be updated by changes to use Heron's theorem

def quadraticEquation():
    return 0


calculus()
print(str(figureTriangle(a, h)))
print(str(figureTrapezoid(a, b, h)))