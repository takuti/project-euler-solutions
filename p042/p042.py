# coding: utf-8

def word2value(w):
  """
  >>> word2value('SKY')
  55
  """
  v = 0
  for c in w:
    v += ord(c) - ord('A') + 1
  return v

def T(n):
  return n * (n+1) / 2

def create_triangle_numbers(upper):
  n = 1
  triangles = []
  while True:
    t = T(n)
    if t > upper: break
    triangles.append(t)
    n += 1
  return triangles


def main():
  words = open('p042_words.txt').read().rstrip().replace('\"','').split(',')
  values = []
  for w in words:
    values.append(word2value(w))
  triangles = create_triangle_numbers(max(values))
  cnt = 0
  for v in values:
    if v in triangles: cnt += 1
  print cnt

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
