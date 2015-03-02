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

def P(n):
  return n * (3 * n - 1) / 2

def minD():
  # generate n pentagonals
  pentagonals = []
  for n in range(1, 10000):
    pentagonals.append(P(n))

  for j in range(10000-2):
    for k in range(j+1, 10000-1):
      s = pentagonals[j] + pentagonals[k]
      d = pentagonals[k] - pentagonals[j]
      if is_in(pentagonals, s) and is_in(pentagonals, d):
        return d
  return -1

def main():
  print minD()

if __name__ == '__main__':
  main()
