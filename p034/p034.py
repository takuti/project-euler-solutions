# coding: utf-8

def factorial(n):
  result = 1
  for i in range(2,n+1):
    result *= i
  return result

def main():
  factorials = [factorial(i) for i in range(0,9+1)]
  n = 10
  total = 0
  while True:
    if len(str(n)) * factorials[9] < n: break
    idxs = map(int, str(n))
    s = sum([factorials[i] for i in idxs])
    if n == s: total += n
    n += 1
  print total

if __name__ == '__main__':
  main()
