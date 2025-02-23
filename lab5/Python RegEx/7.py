import re

def camel(s):
    c = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s)
    return c

snake = "snake_case_example_string"
camell = camel(snake)
print(camell)