class Rectangle:
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def calculate_area(self):
        return  (self.width * self.length)


My_rectangle = Rectangle(5, 10)

print(My_rectangle.calculate_area())