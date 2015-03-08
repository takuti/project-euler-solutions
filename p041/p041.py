# coding: utf-8

import math

def is_prime(n):
  if n == 1: return False
  elif n == 2: return True
  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0: return False
  return True

def is_pandigital(n):
  """
  >>> is_pandigital(2143)
  True
  >>> is_pandigital(2153)
  False
  """
  l = list(str(n))
  if min(l) != '1': return False
  uniq_len = len(set(l))
  if len(l) != uniq_len: return False
  if uniq_len != int(max(l)): return False
  return True

def main():
  ans = 0
  for n in xrange(2143, 987654321+1, 2):
    if not is_pandigital(n): continue
    if not is_prime(n): continue
    ans = n
  print ans

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
