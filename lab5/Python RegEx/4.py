import re

def bool(s):
    m = re.findall('^[A-Z]{1}[a-z]', s)
    if m:
        return True
    else:
        return False
    
r ="Json"
print(bool(r))