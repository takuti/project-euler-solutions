
import math

def is_prime(n):
    """
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    """
    if n == 1: return False
    elif n == 2: return True
    for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
        if n % i == 0: return False
    return True

def main():
    length = 1
    n_spiral = 0

    n_diag = 1
    n_prime = 0

    n = 1
    while True:
        length += 2
        n_spiral += 1
        for i in range(4):
            n += 2 * n_spiral
            n_diag += 1
            if is_prime(n): n_prime += 1
        length = 2 * n_spiral + 1
        if float(n_prime) / n_diag < 0.1: break
    print length

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
