class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_square = self.get_square() + other.get_square()
        for i in range(2, 10):
            if new_square % i == 0:
                return Rectangle(i, int(new_square/i))

    def __mul__(self, n):
        return Rectangle(self.get_square(), n)

    def __str__(self):
        return f'Rectangle ({self.width}, {self.height})'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18

r3 = r1 + r2
assert r3.get_square() == 26

r4 = r1 * 4
assert r4.get_square() == 32