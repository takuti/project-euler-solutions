# coding: utf-8

import math

def main():
  n = 2000000
  l = [True] * (n + 1)
  l[0] = l[1] = False
  head = 2
  # Sieve of Eratosthenes
  while True:
    head += l[head:].index(True)
    if head > int(math.sqrt(n)) + 1: break
    for i in range(head*2, n+1, head): l[i] = False
    head += 1

  # Compute sum of prime
  print sum([i for i in range(2, n+1) if l[i] == True])

if __name__ == '__main__':
  main()
