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

  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0: return False

  return True

def most_consective_prime_sum(upper):
  """ Find a prime which can be written as the sum of the most consective primes under 'upper'
  >>> most_consective_prime_sum(100)
  41
  >>> most_consective_prime_sum(1000)
  953
  """
  primes = [2]
  # Find all primes under 1000000
  for i in range(3, upper):
    if is_prime(i): primes.append(i)
  limit = primes[-1]

  tail = len(primes)
  for w in range(tail-1, 0, -1): # how many consective primes are considered?
    for i in range(0,(tail-w)+1):
      s = sum(primes[i:i+w])
      if s > limit: break
      elif s in primes: return s
  return -1

def main():
  print most_consective_prime_sum(1000000)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
