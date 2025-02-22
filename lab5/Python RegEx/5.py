import re

def bool(s):
    m = re.findall('^a.*b$', s)
    if m:
        return True
    else:
        return False
    
r = 'ajuihgruhjgiojjeiob'
print(bool(r))