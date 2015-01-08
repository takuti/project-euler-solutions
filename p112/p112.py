#coding: utf-8

def is_bouncy(n):
  """
  >>> is_bouncy(134468)
  False
  >>> is_bouncy(66420)
  False
  >>> is_bouncy(155349)
  True
  """
  d = map(int, str(n))
  l = len(d)
  up, down = False, False
  for i in range(l-1):
    if d[i] > d[i+1]: down = True
    elif d[i] < d[i+1]: up = True
    if up and down: return True
  return False


def main():
  n, m = 100, 0
  while True:
    m += 1 if is_bouncy(n) else 0
    if float(m) / n == 0.99: break
    n += 1
  print n

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
