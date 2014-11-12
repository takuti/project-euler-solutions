# coding: utf-8

def spiral(n):
  """ Find the sum of the numbers of the diagonals of nxn spiral
  >>> spiral(5)
  101
  """
  total = 1
  current = 1
  inc = 0
  while True:
    inc += 2
    for j in range(4):
      current += inc
      total += current
    if current == n * n: break
  return total

def main():
  print spiral(1001)


if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
