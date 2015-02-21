# coding: utf-8

import math

def get_primes(limit):
  """ return all primes under given limit
  """
  primes = [2]
  for n in range(3, limit):
    prime_flg = True
    for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
      if n % i == 0:
        prime_flg = False
        break
    if prime_flg: primes.append(n)
  return primes

def get_rotations(n):
  """ return all rotations for given n
  >>> get_rotations(197)
  [197, 971, 719]
  """
  l = [n]
  s = str(n)
  for i in range(1, len(s)):
    l.append(int(s[i:] + s[:i]))
  return l

def is_in(a, n):
  """ find n from sorted-array a
  """
  l = 0
  r = len(a) - 1
  while l <= r:
    mid = (l + r) / 2
    if n == a[mid]: return True
    elif n > a[mid]: l = mid + 1
    else: r = mid - 1
  return False

def count_circular_primes(n):
  """ count circular primes below n
  >>> count_circular_primes(100)
  13
  """
  primes = get_primes(n)
  cnt = 0
  for p in primes:
    rotations = get_rotations(p)
    accept_flg = True
    for rp in rotations:
      if not is_in(primes, rp):
        accept_flg = False
        break
    if accept_flg: cnt += 1
  return cnt

def main():
  print count_circular_primes(1000000)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
