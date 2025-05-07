#Answer: a , b , c
# The code creates a dictionary with integer keys and string values.
d = {0: 'a', 1: 'b', 2: 'c'}
for x in d.values():
   print(x)

#Answer:['H', 'E', 'L', 'L', 'O']
# The code creates a string and converts each character to uppercase using a list comprehension.
a="hello"
b=list(x.upper() for x in a)
print(b)

#Answer:Either 10.4 or 56.99 or 76
# The code randomly selects one of the three numbers from the list and prints it.
import random
print (random.choice([10.4, 56.99, 76]))

#Answer: ['john', 'peter']
# The code creates a dictionary with string keys and integer values and prints the keys as a list.
d = {"john":40, "peter":45}
print(list(d.keys()))

#Answer: 2
# The code creates a dictionary with string keys and integer values and prints the number of items in the dictionary.
total = {}
def insert(item):
   if item in total:
      total[item] += 1
   else:
      total[item] = 1
insert('Banana')
insert('Banana')
insert('Banana')
insert('Apple')
print(len(total))

#Answer:[1, 4, 9, 16, 25]
# The code creates a list of numbers and uses the map function to square each number in the list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

class Car:
 def __init__(self, brand, model):
   self.brand = brand
   self.model = model
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")
print(car1.brand, car1.model)

def factorial(n):
 if n == 0:
   return 1
 else: return n * factorial(n - 1)
print(factorial(5))

for i in range(5):
 if i % 2 == 0:
   continue
 else:
   print(i)

a = 3
for k in range(7,12):
   a=a+a
print(a)

a = 4
for i in range(5):
   a += i 
print(a)

a, *b, c = [1, 2]
print(a, b, c)

def f(a, *pargs, **kargs): print(a, pargs, kargs)
f(1, 2, 3, x=4, y=5)

def get_name_and_decades(name, age):
   print(f"My name is {name} and I'm {age / 10:.5f} decades old.")
get_name_and_decades("Leo", 31)

print(4&8)

teams = ['Astana', 'Qairat', 'Ordabasy']
a, b, c = teams
print(a)

x = float(5)
y = str(x)
print(y)

x = 23
num = 0 if x > 10 else 11
print(num)

x, y, z = "Orange", 231, "Cherry"
print(x)

import datetime
x = datetime.datetime(2023, 5, 17)
print(x)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = set_a.union(set_b)
print(set_c)