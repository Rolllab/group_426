import math


class Circle:
    def __init__(self, radius=0):
        self.radius = radius
        self.pi = math.pi

    def length(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * (self.radius ** 2)

class Rectangle:
    def __init__(self, side=0):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Result:
    def __init__(self, radius:int):
        self.side = radius * 2
        self.circle = Circle(radius)
        self.rectangle = Rectangle(self.side)

    def return_result(self):
        length_circle = self.circle.length()
        area_circle = self.circle.area()
        area_rectangle = self.rectangle.area()
        perimeter_rectangle = self.rectangle.perimeter()
        return (length_circle, area_circle), (area_rectangle, perimeter_rectangle)



if __name__ == '__main__':
    result = Result(10)
    print(result.return_result())
    print(f'Длина окружности = {(result.return_result()[0][0]).__round__(2)}')
    print(f'Площадь круга = {(result.return_result()[0][1]).__round__(2)}')
    print()
    print(f'Площадь квадрата = {result.return_result()[1][0]}')
    print(f'Периметр квадрата = {result.return_result()[1][1]}')
