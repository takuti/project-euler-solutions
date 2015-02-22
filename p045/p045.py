# coding: utf-8

def T(n):
  """
  >>> T(285)
  40755
  """
  return n*(n+1) / 2

def P(n):
  """
  >>> P(165)
  40755
  """
  return n*(3*n-1) / 2

def H(n):
  """
  >>> H(143)
  40755
  """
  return n*(2*n-1)

def main():
  Ps = []
  Hs = []
  n = 144
  while True:
    t = T(n)
    Ps.append(P(n))
    Hs.append(H(n))
    if t in Ps and t in Hs:
      print t
      break
    # Since T(n) has the slowest glow speed, remove unused numbers from Ps and Hs in each step
    Ps = [p for p in Ps if p > t]
    Hs = [h for h in Hs if h > t]
    n += 1

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
