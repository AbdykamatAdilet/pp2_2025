class StringProcessor:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("string: ")

    def printString(self):
        print(self.text.upper())

sp = StringProcessor()
sp.getString()
sp.printString()