def cycle_len(d):
    """return the length of recurring cycle for 1/d
    >>> cycle_len(2)
    0
    >>> cycle_len(3)
    1
    >>> cycle_len(7)
    6
    >>> cycle_len(6)
    1
    """

    numerators = []
    numerator = 10

    while True:
        # keep previous numerators
        numerators.append(numerator)

        # if d is divisible, there is no recurring cycle
        reminder = numerator % d
        if reminder == 0: return 0

        quotient = numerator / d

        # next numerator will be decuple of the reminder
        numerator = reminder * 10

        # new numerator is in history -> here is the starting point of recurring cycle
        if numerator in numerators:
            return len(numerators) - numerators.index(numerator)


def main():
    max_d = max_len = 0
    for d in range(2, 1000):
        l = cycle_len(d)
        if l > max_len: max_d, max_len = d, l
    print '1/%d has a %d-digit recurring cycle' % (max_d, max_len)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
