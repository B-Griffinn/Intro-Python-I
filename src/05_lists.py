# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print('Append 4 to x', x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print('extend y to x', x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print('8 has been removed from x', x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(len(x) - 1, 99)
print('insert 99 into length of x - 1', x)

# Print the length of list x
# YOUR CODE HERE
print(f"The length of x is {len(x)}")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in range(len(x)):
    print(f"{x[i]} * 1000 is", x[i] * 1000)
