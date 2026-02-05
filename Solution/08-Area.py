from math import pi

# Shapes: Square, Rectangle, Triangle, and Circle
"""
Square: B^2
Rectangle: B * H
Triangle: 1/2 * ...
Circle: PI * R^2
"""
from typing import override


class Shape:
    def __init__(self, base: int | float):
        self.base: int | float = base

    def area(self) -> int | float:
        pass

class Square(Shape):
    def __init__(self, base: int | float):
        super().__init__(base)

    @override
    def area(self) -> int | float:
        return self.base ** 2

class Rectangle(Shape):
    def __init__(self, base: int | float, height: int | float):
        super().__init__(base)
        self.height: int | float = height

    @override
    def area(self) -> int | float:
        return self.base * self.height

class Triangle(Shape):
    def __init__(self, base: int | float):
        super().__init__(base)

    @override
    def area(self) -> int | float:
        return (1/2) * self.base    # Not confirm!

class Circle(Shape):
    def __init__(self, radius: int | float):
        super().__init__(radius)

    @override
    def area(self) -> int | float:
        return pi * self.base ** 2


if __name__ == '__main__':
    print("Square:", Square(2).area(), sep='\t\t')
    print("Rectangle:", Rectangle(2, 1.3).area(), sep='\t')
    print("Triangle:", Triangle(2.34).area(), sep='\t')
    print("Circle:", f"{Circle(4.1).area():.4}", sep='\t\t')
