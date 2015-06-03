
import math

def is_prime(n):
  """
  >>> is_prime(41)
  True
  >>> is_prime(42)
  False
  """
  if n == 1: return False
  elif n == 2: return True

  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0: return False

  return True

def is_permutations(n1, n2, n3):
  s1 = sorted(str(n1))
  s2 = sorted(str(n2))
  s3 = sorted(str(n3))
  return s1 == s2 == s3

def main():
  for n1 in range(1000, 10000-(3330*2)):
    n2 = n1 + 3330
    n3 = n2 + 3330
    if is_prime(n1) and is_prime(n2) and is_prime(n3) and is_permutations(n1, n2, n3):
      print str(n1) + str(n2) + str(n3)

if __name__ == '__main__':
  main()
