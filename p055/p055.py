# coding: utf-8

def is_palindrome(n):
  """
  >>> is_palindrome(121)
  True
  >>> is_palindrome(1292)
  False
  """
  l = map(int, str(n))
  m = len(l) / 2

  post = l[m:] if len(l) % 2 == 0 else l[m+1:]
  post.reverse()

  return l[:m] == post

def reverse(n):
  n_list = list(str(n))
  n_list.reverse()
  return int(''.join(n_list))

def main():
  lychrel_cnt = 0
  for i in range(1, 10001):
    iter_cnt = 1
    n = i
    while True:
      n = n + reverse(n)
      if is_palindrome(n): break
      iter_cnt += 1
      if iter_cnt >= 50:
        lychrel_cnt += 1
        break
  print lychrel_cnt

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
