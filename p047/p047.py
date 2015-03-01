# coding: utf-8

import math

def is_prime(n):
  """
  >>> is_prime(41)
  True
  >>> is_prime(42)
  False
  """
  if n == 1: return False
  elif n == 2: return True
  for i in xrange(2, n/2 + 1):
    if n % i == 0: return False
  return True

def find_factors(n):
  factors = []
  for i in xrange(2, n/2 + 1):
    if n % i == 0:
      n /= i
      factors.append(i)
  return factors

def L_consective_and_factors(L):
  """ Return the first number of L-consective numbers to have L-distinct prime factors
  >>> L_consective_and_factors(2)
  14
  >>> L_consective_and_factors(3)
  644
  """
  primes = [2]
  n = 2
  first = consective_cnt = 0
  while True:
    n += 1
    if is_prime(n): # prime numbers do not have any factors
      primes.append(n)
      consective_cnt = 0
      continue
    factors = find_factors(n)
    if len(factors) != L: # do not have L-distinct prime factors
      consective_cnt = 0
      continue
    if set(map(lambda v: v in primes, factors)) == set([True]): # all 4 factors are prime
      if consective_cnt == 0: first = n
      consective_cnt += 1
    else:
      consective_cnt = 0
    if consective_cnt == L: break
  return first

def main():
  print L_consective_and_factors(4)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
