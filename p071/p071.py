# coding: utf-8

def is_coprime(a, b):
  """ check whether given 2 values (a >= b) are coprime based on the euclidean algorithm
  """
  while True:
    r = a % b
    if r == 0: break
    a = b
    b = r
  if b == 1: return True
  else: return False

def main():
  d_limit = 1000000
  target = 3./7. # we want to find the left value of 3/7
  left = ans_numerator = 0
  for d in xrange(2, d_limit+1):
    float_d = float(d)
    inc = 2 if d % 2 == 0 else 1 # if both of d and n are even, they are not coprime
    start = d / 7 * 3 # the loop for numerators will start from the nearest value to 3/7
    for n in xrange(start, d, inc):
      v = n / float_d
      if v >= target: break
      if v <= left: continue
      if is_coprime(d, n):
        left = v
        ans_numerator = n
  print 'the numerator of the fraction immediately to the left of 3/7:', ans_numerator

if __name__ == '__main__':
  main()
