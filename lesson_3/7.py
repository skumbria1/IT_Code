from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = input()
    if n.isdigit():
        print(f'index: {n}, value: {fibonacci(int(n))}')
