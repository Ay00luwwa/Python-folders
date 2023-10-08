import matplotlib.pyplot as plt

# Define the data to be plotted
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot of the data
plt.plot(x, y)

# Set the labels for the x and y axes
plt.xlabel('x')
plt.ylabel('y')

# Set the title of the plot
plt.title('A Simple Line Plot')

# Show the plot
plt.show()