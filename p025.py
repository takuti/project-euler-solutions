# coding: utf-8

def n_digit_fibo(n):
  """ Find the first term in the Fibonacci sequence to contain n digits
  >>> n_digit_fibo(3)
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
  print n_digit_fibo(1000)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
