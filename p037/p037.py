# coding: utf-8

import math

def is_prime(n):
  """
  >>> is_prime(11)
  True
  >>> is_prime(12)
  False
  >>> is_prime(2)
  True
  >>> is_prime(1)
  False
  """
  if n == 1: return False
  elif n == 2: return True
  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0: return False
  return True

def is_truncatable(n):
  """ check whether given prime is truncatable
  >>> is_truncatable(3797)
  True
  """
  s = str(n)
  s_len = len(s)
  if s_len == 1: return False
  # left -> right
  idx = 1
  while idx < s_len:
    if not is_prime(int(s[idx:])): return False
    idx += 1
  # right -> left
  idx = s_len-1
  while idx > 0:
    if not is_prime(int(s[0:idx])): return False
    idx -= 1
  return True

def main():
  total = 0
  cnt = 0
  n = 11
  while True:
    if is_prime(n):
      if is_truncatable(n):
        cnt += 1
        total += n
    if cnt == 11: break
    n += 1
  print total

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
