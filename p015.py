# coding: utf-8

def count_path(n,m):
  """ count the number of paths in (n x m) grid
  This function just compute ${n+m}_C_m$
  >>> count_path(2,2)
  6
  """
  ans = 1
  for i in range(n+m,n,-1):
    ans *= i
  for i in range(m,0,-1):
    ans /= i
  return ans

def main():
  print count_path(20,20)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
