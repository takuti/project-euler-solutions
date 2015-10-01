import itertools

def factorial(n):
    """
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    """
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res

def main():
    pl = list(itertools.combinations_with_replacement([1,2,3,4], 9))
    cl = list(itertools.combinations_with_replacement([1,2,3,4,5,6], 6))

    factorial_9 = factorial(9)
    factorial_6 = factorial(6)

    p_win = 0
    for p in pl:
        p_sum = sum(p)
        for c in cl:
            c_sum = sum(c)
            if p_sum > c_sum:
                p_denominator = 1
                for i in set(p):
                    p_denominator *= factorial(p.count(i))
                p_products = factorial_9 / p_denominator

                c_denominator = 1
                for i in set(c):
                    c_denominator *= factorial(c.count(i))
                c_products = factorial_6 / c_denominator

                p_win += p_products * c_products

    n = (4**9) * (6**6)
    print n, p_win, float(p_win) / n
    print round(float(p_win) / n, 7)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
