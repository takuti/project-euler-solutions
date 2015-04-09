# coding: utf-8

def main():
  n = 1
  cnt = 0
  while True:
    i = 1
    while True:
      l = len(str(i ** n))
      if l > n: break
      if l == n:
        cnt += 1
        print '[%d] %d = %d^%d' % (cnt, i**n, i, n)
      i += 1
    n += 1


if __name__ == '__main__':
  main()
