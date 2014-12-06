# coding: utf-8

def n_digits_fibo_term(n):
  """ Find the first term in the Fibonacci sequence to contain n digits
  >>> n_digits_fibo_term(3)
  12
  """
  f1 = 1
  f2 = 1
  term_cnt = 2
  while True:
    f = f1 + f2
    term_cnt += 1
    if f / (10 ** (n-1)) != 0:
      return term_cnt
    f1 = f2
    f2 = f

def main():
  print n_digits_fibo_term(1000)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
