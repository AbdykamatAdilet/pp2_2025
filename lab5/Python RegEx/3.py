import re

def bool(s):
    m = re.findall("[a-z]_[a-z]", s)
    if m:
        return True
    else:
        return False
    
r = 'Axokna_kcsnicnojk'
print(bool(r))