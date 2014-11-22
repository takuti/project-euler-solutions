# coding: utf-8

def is_evenly_divisible(n):
  for i in range(2, 21):
    if n % i != 0: return False
  return True

def main():
  n = 2520
  while not(is_evenly_divisible(n)):
    # always, odd numbers are not dinisible by 2
    n += 2
  print n

if __name__ == '__main__':
  main()
