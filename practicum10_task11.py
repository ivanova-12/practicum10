def is_prime(num: int) -> bool:
    """Check if number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_primes() -> None:
    """Print all prime numbers before N"""
    N = input()
    try:
        N = int(N)
    except ValueError:
        raise ValueError('Неверный ввод')

    for num in range(1, N + 1):
        if is_prime(num):
            print(num, end=' ')
