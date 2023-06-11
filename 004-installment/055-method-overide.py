class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x*self.y
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14*super().area() # area of a circle pi*r^2



rect = shape(5, 4)
print(rect.area())

c = circle(5)
print(c.area())