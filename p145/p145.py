# coding: utf-8

def is_reversible(n, rn):
  """
  >>> is_reversible(36, 63)
  True
  >>> is_reversible(409, 904)
  True
  """
  for c in str(n + rn):
    if int(c) % 2 == 0: return False
  return True

def main():
  cnt = 0
  below = 1000000000
  for i in xrange(below):
    if i % 1000000 == 0: print i, cnt
    if i % 10 == 0: continue
    r = int(str(i)[::-1])
    if r < i or (i % 2 == r % 2): continue
    if is_reversible(i, r): cnt += 2
  print cnt

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
