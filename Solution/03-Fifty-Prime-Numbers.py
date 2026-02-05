def is_prime(number: int) -> bool:
    if number < 1:
        return False
    elif number == 1 or number == 2:
        return True

    for n in range(2, number):
        if number % n == 0:
            return False
    return True


if __name__ == '__main__':
    count: int = 0
    number: int = 1
    while count < 50:
        if is_prime(number):
            print(number)
            count += 1
        number += 1
