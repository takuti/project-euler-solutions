# coding: utf-8

import math

def trial_division(n):
  factors = []

  for i in xrange(2, (int(math.sqrt(n)) + 1) + 1):
    if n % i == 0:
      n /= i
      factors.append(i)

  return factors

def main():
  n = input('> ')
  print trial_division(n)

if __name__ == '__main__':
  main()
