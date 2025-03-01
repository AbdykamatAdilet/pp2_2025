from functools import reduce

def list(numbers):
    def multiply(x, y):
        return x * y
    
    return reduce(multiply, numbers)

nums = [2, 3, 7, 9, 88]
print(list(nums))