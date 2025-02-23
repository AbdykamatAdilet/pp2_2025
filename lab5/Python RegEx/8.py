import re

def split(i):
    s = re.sub(r'([A-Z])', r' \1', i).split()
    return s

Example = "SplitThisStringAtUpperCaseLetters"
res = split(Example)
print(res)