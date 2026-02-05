def is_prime(number: int) -> bool:
    # print(f"\nChecking for {number}...")

    if number < 1:
        return False
    elif number == 1 or number == 2:
        return True

    for n in range(2, number):
        # print(n, number % n, sep=' --- ')
        if number % n == 0:
            return False
    return True

if __name__ == '__main__':
    print(is_prime(1))
    print(is_prime(13))
    print(is_prime(38))
