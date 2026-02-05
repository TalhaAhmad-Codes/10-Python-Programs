class Binary:
    def __init__(self, number: str):
        self.number: str = number

    @staticmethod
    def is_valid(number: str) -> bool:
        for digit in number:
            if digit not in '01':
                return False
        return True


class Decimal:
    def __init__(self, number: int):
        self.number: int = number


def to_binary(number: Decimal) -> Binary:
    """ Function to convert a decimal number to binary """
    binary: str = ""
    num: int = number.number
    base: int = 2
    while num > 0:
        binary = str(num % base) + binary
        num = int(num / base)

    return Binary(binary)

def to_decimal(number: Binary) -> Decimal:
    """ Function to convert a binary number to decimal """
    decimal: int = 0
    binary: str = number.number
    base: int = 2
    power: int = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * base ** power
        power -= 1

    return Decimal(decimal)

if __name__ == '__main__':
    decimal: Decimal = Decimal(2229)
    binary: Binary = to_binary(decimal)

    print(decimal.number)
    print(binary.number)
    print(to_decimal(binary).number)
