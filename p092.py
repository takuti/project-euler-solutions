# coding: utf-8

def arrive_at(n):
  """ Create chain and return the arrived number
  >>> arrive_at(44)
  1
  >>> arrive_at(85)
  89
  """
  while True:
    n = sum(map(lambda c: int(c)**2, str(n)))
    if n == 1 or n == 89: break
  return n


def main():
  cnt = 0
  for i in xrange(1, 10000000):
    if arrive_at(i) == 89: cnt += 1
  print cnt

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
