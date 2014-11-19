# coding: utf-8

def is_palindrome(n):
  l = map(int, str(n))

  if len(l) % 2 != 0: return False

  m = len(l) / 2
  post = l[m:]
  post.reverse()

  return l[:m] == post


def main():
  largest = 0
  # brute force
  for i in range(100, 1000):
    for j in range(100, 1000):
      n = i * j
      if n > largest and is_palindrome(n):
        largest = n
  print largest

if __name__ == '__main__':
  main()
