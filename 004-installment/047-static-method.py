class Math:
    
    def __init__(self, num):
        self.num = num

    def addNum(self, n):
        self.num += n

    @staticmethod
    def sum(a, b): # Static method is used in inside a class without self argument
        return a + b
    
a = Math(5)
print(a.num)

a.addNum(6)
print(a.num)

print(a.sum(5, 6))
