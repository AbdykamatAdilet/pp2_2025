import time
import math

num = int(input("Write first num:"))
mil = int(input("Write second num:"))

time.sleep(mil / 1000)
result = math.sqrt(num)

print(f"Square root of {num} after {mil} milliseconds is {result}")