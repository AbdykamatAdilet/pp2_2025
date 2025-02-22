import re

def bool(s):
    m = re.findall("ab{2,3}", s)
    if(m):
        return True
    else:
        return False
    
r = 'ab'
print(bool(r))