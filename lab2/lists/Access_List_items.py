#Print the second item of the list:
thisList = ["apple", "banana", "cherry"]
print(thisList[1])

#The first item has index 0.

#Print the last item of the list:
thisList = ["apple", "banana", "cherry"]
print(thisList[-1])

# Return the third, fourth, and fifth item:
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")