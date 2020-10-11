import matplotlib.pyplot as plt
# funkcja y = 5x - 2


X = [i+1 for i in range(0,10)]  # generating 10 points on the Y axis
Y = [5*i - 2 for i in X]        # generating values on the Y axis


plt.plot(X,Y,'ro--')
plt.show()