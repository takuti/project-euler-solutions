
def digital_sum(n):
    """return digital sum of first 100 decimal digits for sqrt(n)
    >>> digital_sum(2)
    475
    >>> digital_sum(100)
    0
    """

    from decimal import getcontext, Decimal
    getcontext().prec = 110
    res = str(Decimal(n).sqrt())
    if '.' not in res: return 0
    point_i = res.index('.')
    res_r = res[:point_i]
    res_f = res[point_i+1:point_i+(101-len(res_r))]
    return sum(map(int, res_r)) + sum(map(int, res_f))

def main():
    total = 0
    for n in range(1, 101):
        total += digital_sum(n)
    print total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
