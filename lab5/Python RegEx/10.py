import re

def snake(i):
    b = re.sub(r'(?<!^)([A-Z])', r'_\1', i ).lower()
    return b

example = "camelCaseExampleString"
res = snake(example)
print(res)