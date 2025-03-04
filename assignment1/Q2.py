# 2. Type Conversion in Python
"""
Python automatically performs implicit type conversion when necessary.
For example, adding an integer and a float results in a float:

x = 5  # int
y = 2.5  # float
z = x + y  # Implicitly converts x to float
print(z, type(z))  # Output: 7.5 <class 'float'>

Explicit type conversion requires functions like int(), float(), list(), str().
Example: Converting string to list:

s = "hello"
lst = list(s)
print(lst)  # Output: ['h', 'e', 'l', 'l', 'o']
"""