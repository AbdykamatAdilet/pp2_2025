#The Python print() function is often used to output variables.

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #the result is:"Python is awesome"

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #the result is: "Pythonisawesome"

x = 5
y = 10
print(x + y)

#notacceptable
x = 5
y = "John"
print(x + y)

#acceptable
x = 5
y = "John"
print(x, y)