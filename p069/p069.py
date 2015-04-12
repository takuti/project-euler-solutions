# coding: utf-8

def is_in(a, n):
  """ find n from sorted-array a
  """
  l = 0
  r = len(a) - 1
  while l <= r:
    mid = (l + r) / 2
    if n == a[mid]: return True
    elif n > a[mid]: l = mid + 1
    else: r = mid - 1
  return False

def phi(n):
  """ return the number of relatively primes for n
  >>> phi(2)
  1
  >>> phi(6)
  2
  >>> phi(9)
  6
  """
  primes = range(2, n)
  cnt = 0
  while len(primes) != cnt:
    x = primes[cnt]
    # if the number is not prime, all multiples of the number must not be prime.
    if n % x == 0: primes = [v for v in primes if v % x != 0]
    else: cnt += 1
  return cnt + 1 # 1 is a relatively prime for all n

def main():
  vmax = nmax = 0
  increase = 2
  n = 2
  while n <= 1000000:
    v = float(n) / phi(n)
    if v > vmax:
      # print n, '\t', v
      vmax = v
      nmax = n
      increase = n
    n += increase
  print 'the max value is', vmax, 'when n =', nmax

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
