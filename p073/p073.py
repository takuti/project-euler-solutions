# coding: utf-8

import math

def is_coprime(a, b):
  """ check whether given 2 values (a >= b) are coprime based on the euclidean algorithm
  """
  while True:
    r = a % b
    if r == 0: break
    a = b
    b = r
  if b == 1: return True
  else: return False

def main():
  d_limit = 1000000
  d_limit = 12000
  l = 1./3.
  r = 1./2.
  cnt = 0
  for d in xrange(2, d_limit+1):
    float_d = float(d)
    start = max(1, d / 3) # the loop for numerators will start from the nearest value to 1/3
    end = int(math.ceil(d / 2))
    # if both of d and n are even, they are not coprime
    inc = 2 if d % 2 == 0 else 1
    if inc == 2 and start % 2 == 0: start += 1
    for n in xrange(start, end+1, inc):
      v = n / float_d
      if v >= r: break
      if v <= l: continue
      if is_coprime(d, n): cnt += 1
  print cnt

if __name__ == '__main__':
  main()
