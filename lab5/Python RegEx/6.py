import re
txt = input("String: ")
x = re.sub("[,. ]", ":" , txt)
print(x)