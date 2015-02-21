# coding: utf-8

import math

def is_prime(n):
  """ Return whether given number is prime, or not based on the trial division
  >>> is_prime(41)
  True
  >>> is_prime(40)
  False
  """
  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0:
      n /= i
      return False
  return True

def main():
  max_product = max_cnt = 0
  for a in range(-999, 1000):
    for b in range(-999, 1000):
      f = lambda n: n ** 2 + a * n + b
      n = 0
      while True:
        fn = f(n)
        if (fn < 0) or (not is_prime(fn)): break
        n += 1
      if n > max_cnt:
        max_cnt = n
        max_product = a * b
  print max_product

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
