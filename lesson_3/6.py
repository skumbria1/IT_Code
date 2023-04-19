from math import sqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    number = input()
    if number.isdigit():
        print('Простое') if is_prime(int(number)) else print('Составное')
    else:
        print('n must be valid')
