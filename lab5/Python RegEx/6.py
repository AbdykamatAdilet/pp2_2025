import re

def space(i):
    x = re.sub("[,. ]", ":" , i)
    return x

example = "You,me. III"
res = space(example)
print(res)