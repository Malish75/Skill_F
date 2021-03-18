class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def figure_as_str(self):
        print(f"Ширина - {self.width}, высота - {self.height}")


a = Rectangle(1,2)
a.figure_as_str()