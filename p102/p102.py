# coding: utf-8

import math

def cross((ax, ay), (bx, by)):
  """ conpute cross product of given 2 vectors vector(a) and vector(b)
  return only z-axis element
  """
  return ax*by - bx*ay

def is_in_triangle(x0, y0, x1, y1, x2, y2):
  """ Check the origin (0, 0) is in a triangle define by (x0,y0), (x1,y1), (x2,y2)
  <=> direction of cross products must be same
  """
  c1 = cross((x1-x0, y1-y0), (0-x1, 0-y1))
  c2 = cross((x2-x1, y2-y1), (0-x2, 0-y2))
  c3 = cross((x0-x2, y0-y2), (0-x0, 0-y0))
  if (c1 > 0 and c2 > 0 and c3 > 0) or (c1 < 0 and c2 < 0 and c3 < 0): return True
  return False

def main():
  triangles = open('p102_triangles.txt').readlines()
  cnt = 0
  for t in triangles:
    p = map(int, t.rstrip().split(','))
    if is_in_triangle(p[0], p[1], p[2], p[3], p[4], p[5]): cnt += 1
  print cnt

if __name__ == '__main__':
  main()
