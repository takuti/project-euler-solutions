# coding: utf-8

def find_nearest_grid(n):
  """ find the size of rectangler grid which has n rectangles
  >>> find_nearest_grid(18)
  (3, 2)
  """
  w = 1
  total = 0
  min_error = float('inf')
  keep_cnt = 0 # how many continuous grids do not provide minimum error?
  while True:
    for h in range(1, w+1):
      total = 0
      for i in range(w, 0, -1):
        for j in range(h, 0, -1):
          total += (i * j)
      e = abs(total - n)
      if e < min_error:
        min_error = e
        nearest_size = (w, h)
        keep_cnt = 0
      else:
        keep_cnt += 1
      if e == 0 or keep_cnt > 10000: return nearest_size ### NO GOOD: 10000 is heuristic decision
    w += 1

def main():
  w, h = find_nearest_grid(2000000)
  print w * h

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
