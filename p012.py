# coding: utf-8

def divisors(x):
  l = []
  i = 1
  while i * i <= x:
    if x % i == 0:
      l.append(i)
      if i != x / i: l.append(x / i)
    i += 1
  return l

def find(n):
  """ Find the triangle number having 500 divisors
  >>> find(5)
  28
  """
  i = 1
  triangle = 0
  while len(divisors(triangle)) < n:
    triangle += i
    i += 1
  return triangle

def main():
  print find(500)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
