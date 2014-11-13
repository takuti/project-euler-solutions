# coding: utf-8

def sum_of_divisors(n):
  """ Compute the sum of proper divisors of n
  >>> sum_of_divisors(220)
  284
  """
  return sum([i for i in range(1,n/2+1) if n%i == 0])

def is_amicable(a, b):
  return a!=b and sum_of_divisors(b) == a

def main():
  s = 0
  past_a = []
  for a in range(1,10000+1):
    b = sum_of_divisors(a)
    if b in past_a: continue
    if not is_amicable(a, b): continue

    s += a + b
    past_a.append(a)
  print s

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
