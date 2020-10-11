import matplotlib.pyplot as plt

#   plt.plot(numbers, ‘o’) - unconnected points
#   plt.plot(numbers, ‘.’) - unconnected dots
#   plt.plot(numbers, ‘s’) - niepołączone squares
#   plt.plot(numbers, ‘ro’) - red points
#   plt.plot(numbers, ‘g^’) - green triangles
#   plt.plot(numbers, ‘k*’) - black stars
#   plt.plot(numbers, ‘r-’) - points connected by red lines
#   plt.plot(numbers, ‘bD:’) - blue diamonds connected by dots
#   plt.plot(numbers, ‘mp--’) - pink pentagons connected by dashed lines

numbers = [5, 10, 15, 3, 20]

plt.plot(numbers, 'o')

plt.show()