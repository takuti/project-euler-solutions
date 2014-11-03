# coding: utf-8

def sum_of_squares(n):
  """ Compute sum of squares of the first n natural numbers
  >>> sum_of_squares(10)
  385
  """
  return sum(map(lambda x: x ** 2, range(1,n+1)))

def square_of_sum(n):
  """ Compute square of sum of the first n natural numbers
  >>> square_of_sum(10)
  3025
  """
  return sum(range(1,n+1)) ** 2

def main():
  print square_of_sum(100) - sum_of_squares(100)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
