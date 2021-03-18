class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f'{type(a).__name__}({self.x}, {self.y},{self.width},{self.height})'


a = Rectangle(1,2,3,4)
print(a)