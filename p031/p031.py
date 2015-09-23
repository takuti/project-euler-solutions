# coding: utf-8

def ways(p, coins):
    """
    >>> ways(1, [1, 2, 5, 10, 20, 50, 100, 200])
    1
    >>> ways(2, [1, 2, 5, 10, 20, 50, 100, 200])
    2
    >>> ways(3, [1, 2, 5, 10, 20, 50, 100, 200])
    2
    """
    if p == 0: return 1

    cnt = 0
    n_coin = len(coins)
    for i in range(n_coin):
        coin = coins[i]
        max_n = p / coin
        for n in range(1, max_n+1):
            cnt += ways(p - (coin * n), coins[i+1:])
    return cnt

def main():
    print ways(200, [1, 2, 5, 10, 20, 50, 100, 200])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
