# coding: utf-8

def factorial(n):
  """
  >>> factorial(0)
  1
  >>> factorial(5)
  120
  """
  fact = 1
  for i in range(2, n+1):
    fact *= i
  return fact

def C(n, r):
  return factorial(n) / (factorial(r) * factorial(n-r))

def main():
  cnt = 0
  for n in range(1, 101):
    for r in range(n+1):
      if C(n, r) > 1000000: cnt += 1
  print cnt

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
