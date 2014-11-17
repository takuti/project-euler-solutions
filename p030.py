# coding: utf-8

def main():
  n = 2
  s = 0
  while True:
    # THIS LOOP DOES NOT STOP
    if  sum(map(lambda i: int(i) ** 5, str(n))) == n:
      s += n
      print '%d (total: %d)' % (n, s)
    n += 1


if __name__ == '__main__':
  main()
