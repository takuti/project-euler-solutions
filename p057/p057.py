def N_th_expansion(N):
    """return (numerator, denominator) of N-th expansion
    >>> N_th_expansion(1)
    (3, 2)
    >>> N_th_expansion(4)
    (41, 29)
    >>> N_th_expansion(8)
    (1393, 985)
    """
    numerator, denominator = 3, 2

    prev_sub_numerator = 1
    for n in range(1, N):
        next_denominator = 2 * denominator + prev_sub_numerator
        numerator = denominator + next_denominator
        prev_sub_numerator = denominator
        denominator = next_denominator

    return (numerator, denominator)

def main():
    numerator, denominator = 3, 2
    prev_sub_numerator = 1

    cnt = 0
    for i in range(1000): # in the first one-thousand expansions
        if len(str(numerator)) > len(str(denominator)): cnt += 1

        next_denominator = 2 * denominator + prev_sub_numerator
        numerator = denominator + next_denominator
        prev_sub_numerator = denominator
        denominator = next_denominator
    print cnt

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
