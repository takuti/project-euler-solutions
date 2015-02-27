# coding: utf-8

def digital_sum(a, b):
  """ return the digital sum of a^b
  >>> digital_sum(10, 100)
  1
  >>> digital_sum(100, 100)
  1
  """
  digits = map(int, str(a ** b))
  return sum(digits)

def main():
  max_sum = 0
  for a in range(100):
    for b in range(100):
      s = digital_sum(a, b)
      if max_sum < s: max_sum = s
  print max_sum

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
