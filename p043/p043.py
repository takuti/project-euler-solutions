from itertools import permutations

def get_all_0to9_pandigitals():
    pandigitals = []
    for permutation in permutations(range(10), 10):
        str_n = ''.join(map(str, list(permutation)))
        if str_n[0] != '0': pandigitals.append(int(str_n))
    return pandigitals

def is_satisfy_propaty(n):
    """
    >>> is_satisfy_propaty(1406357289)
    True
    """
    s = str(n)
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(s[i:i+3]) % primes[i-1] != 0: return False
    return True

def main():
    total = 0
    pandigitals = get_all_0to9_pandigitals()
    for n in pandigitals:
        if is_satisfy_propaty(n):
            print n
            total += n
    print total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
