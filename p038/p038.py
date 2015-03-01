# coding: utf-8

def is_pandigital(s):
  """ Check whether given string-number is 1 to 9 pandigital
  """
  set_s = set(s)
  if len(set_s) == 9 and '0' not in set_s: return True
  return False

def main():
  max_pandigital = 0
  i = 1
  while True:
    concatinate = str(i * 1)
    n = 2
    while True:
      concatinate += str(i * n)
      l = len(concatinate)
      num_concatinate = int(concatinate)
      if l > 9: break
      elif l == 9 and is_pandigital(concatinate) and max_pandigital < num_concatinate:
        print 'i = %d, n = %d, concatinate = %d' % (i, n, num_concatinate)
        max_pandigital = num_concatinate
        break
      n += 1
    i += 1
    if i == 333333333: break

if __name__ == '__main__':
  main()
