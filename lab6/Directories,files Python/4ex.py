import os

def count(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

print(count("test.txt"))