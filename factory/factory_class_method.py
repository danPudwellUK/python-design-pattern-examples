class Triangle:
    def __init__(self, side1_length, side2_length, side3_length):
        self.side1_length = side1_length
        self.side2_length = side2_length
        self.side3_length = side3_length

    @classmethod
    def createEquilateral(cls, length):
        return cls(length, length, length)

    def display(self):
        if self.side1_length == self.side2_length == self.side3_length:
            print("equilateral")
        elif self.side1_length == self.side2_length or self.side1_length == self.side3_length or self.side2_length == self.side3_length:
            print("isosceles")
        else:
            print("scalene")


equliateral_triangle = Triangle.createEquilateral(10)
equliateral_triangle.display()

isosceles_triangle = Triangle(10, 10, 9)
isosceles_triangle.display()

scalene_triangle = Triangle(10, 14, 9)
scalene_triangle.display()


# classmethod perserves object inheritance, staticmethod does not