"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
import platform
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for i in sys.argv:
    print('\nI am each sys.argv', i)

# Print out the OS platform you're using:
# YOUR CODE HERE
print(
    f'I am using the {platform.system()} platform aka {sys.getwindowsversion()}')

# Print out the version of Python you're using:
# YOUR CODE HERE
print(f"I am using Python version: {sys.version} ")


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f"The current process ID is: {os.getpid()} ")

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f"My current workind id is: {os.getcwd()}")

# Print out your machine's login name
# YOUR CODE HERE
print(f"My machines login name is: {os.getlogin()}\n")
