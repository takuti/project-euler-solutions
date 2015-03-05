# coding: utf-8

def is_same(n1, n2):
  """
  >>> is_same(125874, 251748)
  True
  >>> is_same(125875, 251748)
  False
  """
  return sorted(list(str(n1))) == sorted(list(str(n2)))

def is_same_2to6(x):
  for i in range(2, 7):
    if not is_same(x, i*x): return False
  return True

def main():
  x = 0
  while True:
    x += 1
    if is_same_2to6(x): break
  print x

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
