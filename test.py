import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create a plot
plt.plot(x, y)

# Set custom x-axis ticks
plt.xticks([0, 1, 2, 3, 4, 5], ['zero', 'one', 'two', 'three', 'four', 'five'])

# Display the plot
plt.show()
