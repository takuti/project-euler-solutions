# coding: utf-8

def factorial(n):
  """
  >>> factorial(5)
  120
  """
  result = 1
  for i in xrange(2, n+1):
    result *= i
  return result

def next_term(s):
  """ Compute the next term of given term
  >>> next_term(69)
  363600
  """
  digits = map(int, str(s))
  total = 0
  for d in digits:
    total += factorial(d)
  return total


def chain(s):
  c = []
  while True:
    c.append(s)
    t = next_term(s)
    if t in c: return len(c)
    s = t

def main():
  cnt = 0
  for i in xrange(1000000):
    if chain(i) == 60: cnt += 1
  print cnt

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
