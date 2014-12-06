# coding: utf-8

import math

def main():
  n = 3
  cnt = 1
  while True:
    # Trial Division
    for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
      if n % i == 0:
        cnt -= 1
        break
    cnt += 1
    if cnt == 10001: break
    n += 2
  print n

if __name__ == '__main__':
  main()
