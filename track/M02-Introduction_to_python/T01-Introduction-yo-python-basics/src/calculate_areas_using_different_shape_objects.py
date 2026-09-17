class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Input values
length = int(input())
breadth = int(input())
side = int(input())

# Object creation
rect = Rectangle(length, breadth)
sq = Square(side)

# Store objects in a list
shapes = [rect, sq]

# Call area() on each object using a loop
for shape in shapes:
    print(shape.area())