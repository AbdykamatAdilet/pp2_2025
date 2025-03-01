def count(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

text = "Hello World"
upper, lower = count(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
