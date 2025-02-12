import math
class Value():
    def __init__(self,value):
        self.value = value
    
    def v(self):
        print(math.sqrt(self.value))
a = Value(5)
a.v()