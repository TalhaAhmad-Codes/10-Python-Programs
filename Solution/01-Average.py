def average(*args: int | float) -> float:
    return sum(args) / len(args)

if __name__ == '__main__':
    print(average(1, 3))
    print(average(1, 3, 5))
