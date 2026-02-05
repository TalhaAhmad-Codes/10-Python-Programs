from math import remainder


class Complex:
    def __init__(self, real: int, imaginary: int):
        self.real: int = real
        self.imaginary: int = imaginary

    def __add__(self, other: 'Complex') -> 'Complex':
        """
        Formula:
        (a + bi) + (c + di) = (a + b) + (c + d)i
        """
        real: int = self.real + other.real
        imaginary: int = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __sub__(self, other: 'Complex') -> 'Complex':
        """
        Formula:
        (a + bi) - (c + di) = (a - b) + (c - d)i
        """
        real: int = self.real - other.real
        imaginary: int = self.imaginary - other.imaginary
        return Complex(real, imaginary)

    def __mul__(self, other: 'Complex') -> 'Complex':
        """
        Formula:
        (a + bi) * (c + di) = a(c + di) + bi(c + di)
                            = a*c + a*di + b*ci - b*d   // i^2 = -1
                            = (a*c - b*d) + (a*d + b*c)i
        """
        real: int = self.real * other.real - self.imaginary * other.imaginary
        imaginary: int = self.real * other.imaginary + self.imaginary + other.real
        return Complex(real, imaginary)

    def __truediv__(self, other: 'Complex') -> 'Complex':
        """
        Formula:
        (a + bi) / (c + di) = [(a + bi) / (c + di)] * [(c - di) / (c - di)]
                            = [(a + bi) * (c - di)] / [(c + di) * (c - di)]
                            = [a(c - di) + bi(c - di)] / [(c^2) - (di)^2]
                            = (a*c - a*di + b*ci + b*d) / (c^2 + d^2)       // i^2 = -1
                            = [(a*c + b*d) + (b*c - a*d)i] / (c^2 + d^2)
                            = [(a*c + b*d) / (c^2 + d^2)] + [(b*c - a*d) / (c^2 + d^2)]i
        """
        # (c^2 + d^2)
        result: int = other.real ** 2 + other.imaginary ** 2
        real: int = int((self.real * other.real + self.imaginary * other.imaginary) / result)
        imaginary: int = int((self.imaginary * other.real - self.real * other.imaginary) / result)
        return Complex(real, imaginary)

    def __repr__(self) -> str:
        operator: str = '+' if self.imaginary >= 0 else '-'
        return f"{self.real} {operator} {abs(self.imaginary)}i"

if __name__ == '__main__':
    num1, num2 = Complex(1, 2), Complex(3, 4)
    print("Addition:", f"({num1}) + ({num2})", '=', num1 + num2, sep=' ')
    print("Subtraction:", f"({num1}) - ({num2})", '=', num1 - num2, sep=' ')
    print("Multiplication:", f"({num1}) * ({num2})", '=', num1 * num2, sep=' ')
    print("Division:", f"({num1}) / ({num2})", '=', num1 / num2, sep=' ')
