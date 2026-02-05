is_even = lambda number : number % 2 == 0
is_odd = lambda number : number % 2 == 1

def sum_evens(size: int = 100) -> int:
    count: int = 0
    number: int = 0
    sum: int = 0
    while count < size:
        if is_even(number):
            sum += number
            count += 1
        number += 1
    return sum

def sum_odds(size: int = 100) -> int:
    count: int = 0
    number: int = 0
    sum: int = 0
    while count < size:
        if is_odd(number):
            sum += number
            count += 1
        number += 1
    return sum

if __name__ == '__main__':
    print("Even Sum:", sum_evens(), sep='\t')
    print("Odd Sum:", sum_odds(), sep='\t')
