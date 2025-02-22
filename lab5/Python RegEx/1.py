import re

def bool(s):
    m = re.findall(r'ab*', s)
    if(m):
        return True
    else:
        return False
    
        
r = 'a'
print(bool(r))