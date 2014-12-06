# coding: utf-8

def generate_seq(n):
  cnt = 1
  while n != 1:
    n = (n / 2) if (n % 2 == 0) else (3 * n + 1)
    cnt += 1
  return cnt


def main():
  max_l, start = 0, 0
  for i in range(2, 1000000):
    l = generate_seq(i)
    if max_l < l:
      max_l = l
      start = i
  print start

if __name__ == '__main__':
  main()
