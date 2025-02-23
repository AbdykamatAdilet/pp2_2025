import re

def space(i):
    res = re.sub(r'(?<!^)(?=[A-Z])', ' ', i)
    return res

example = "SpacesSpaceSpacSpaSpS"
res = space(example)
print(res)