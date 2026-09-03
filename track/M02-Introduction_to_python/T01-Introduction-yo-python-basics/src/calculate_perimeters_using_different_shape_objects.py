class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        # Write your code here
        return 2 * (self.length + self.breadth)


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        # Write your code here
        return 4 * self.side


length = int(input())
breadth = int(input())
side = int(input())

rect = Rectangle(length, breadth)
sq = Square(side)

shapes = [rect, sq]

for shape in shapes:
    print(shape.perimeter())