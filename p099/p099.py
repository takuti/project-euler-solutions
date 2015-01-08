# coding: utf-8

import math

def main():
  lines = open('p099_base_exp.txt').readlines()
  pairs = map(lambda l: map(int, l.rstrip().split(',')), lines)
  n = 0
  max_v = 0
  max_n = 0
  for p in pairs:
    n += 1
    v = p[1] * math.log(p[0])
    if max_v < v:
      max_v = v
      max_n = n
  print max_n

if __name__ == '__main__':
  main()
