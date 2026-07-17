import math


def if_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    upper_limit = int(math.sqrt(n) + 1)
    for i in range(3, upper_limit, 2):
        if n % i == 0:
            return False

    return True


def n_primes(n: int):
    for i in range(2, n + 1):
        if if_prime(i):
            print(f"{i} is a prime number")


n_primes(35)
