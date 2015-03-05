# coding: utf-8

import math

def is_prime(n):
  if n == 1: return False
  elif n == 2: return True

  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0: return False

  return True

def can_written(n, primes):
  """ whether given odd composite number can be written as the sum of a prime and twice a square
  primes: all primes which are less than n
  """
  for p in primes:
    i = 1
    while True:
      v = p + 2 * (i ** 2)
      if v == n: return True
      elif v > n: break
      i += 1
  return False


def main():
  primes = [2]
  n = 3
  while True:
    if is_prime(n):
      primes.append(n)
    elif not can_written(n, primes):
      print n
      break
    n += 2

if __name__ == '__main__':
  main()
