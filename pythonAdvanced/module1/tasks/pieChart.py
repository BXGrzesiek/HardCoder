import matplotlib.pyplot as plt

expenses = ["FLAT", "MEDIA", "FOOD", "ENTERTAINMENT", "LEARNING", "INVESTMENTS"]
values = [3000, 300, 1000, 500, 200, 1500]

plt.pie(values, labels = expenses)
plt.axis('equal') # axle alignment (equal circle)

plt.show()