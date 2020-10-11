import matplotlib.pyplot as plt

expenses = ["FLAT", "MEDIA", "FOOD", "ENTERTAINMENT", "LEARNING", "INVESTMENTS"]
values = [3000, 300, 1000, 500, 200, 1500]

explode = [0 for i in expenses]                     # an array of zeros with the size of expenses
explode[expenses.index("INVESTMENTS")] = 0.1        # replace one of the elements with an offset of 0.1

plt.pie(values, labels = expenses,
    explode = explode,      # highlighting elements according to the pattern
    autopct = "%.2f %%",    # percentages in accordance with the pattern .2f and the percent sign "%%"
    shadow = True           # adding a shadow to the chart

    )
plt.axis('equal')           # axle alignment (equal circle)
plt.show()