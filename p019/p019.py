# coding: utf-8

def is_leap(y):
  if y % 400 == 0:
    return True
  if (y % 100 == 0) or (y % 4 != 0):
    return False
  else:
    return True

def days(y, m):
  if m == 2:
    return 28 + is_leap(y)
  elif m in [4, 6, 9, 11]:
    return 30
  else:
    return 31

def print_1st_day(y,m,d):
  l = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  print '%d.%2d: %s' % (y,m,l[d])

def main():
  cnt = 0
  # 0: Sun, 1: Mon, 2: Tue ..., 6: Sat
  # initial day, Jan 1, 1901, is Tuesday
  d = 2
  for y in range(1901, 2000+1):
    for m in range(1, 12+1):
      if y == 2000 and m == 12: break
      d = (d + (days(y, m) % 7)) % 7 # d loops on mod-7
      if d == 0: cnt += 1
  print cnt

if __name__ == '__main__':
  main()
