class yogesh:
    def __init__(self,n,o,p):
        self.name = n
        self.num = o
        self.percent = p
    def display(self):
        print("name is :",self.name)
        print("num is  : ",self.num)
        print("percent : ",self.percent)
d = yogesh("upojo",98,66)
d.display()