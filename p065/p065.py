# coding: utf-8

def nth_numerator(n):
  """ return the numerator of the n-th convergents for e = [2; 1,2,1,1,4,1,...,1,2k,1,...]
  >>> nth_numerator(1)
  2
  >>> nth_numerator(2)
  3
  >>> nth_numerator(10)
  1457
  """
  init = 2
  if n == 1: return init
  denos = []
  k = 1
  for i in range(0, n-1+3, 3):
    denos.append(1)
    denos.append(2 * k)
    denos.append(1)
    k += 1
  numes = [1] * (n-1)
  for i in range(n-2, 0, -1):
    denos[i-1] = denos[i-1] * denos[i] + numes[i]
    numes[i-1] = denos[i]
  return denos[0] * init + numes[0]

def main():
  print sum(map(int, str(nth_numerator(100))))

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
