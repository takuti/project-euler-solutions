# coding: utf-8

def is_palindrome(n):
  l = map(int, str(n))
  m = len(l) / 2

  post = l[m:] if len(l) % 2 == 0 else l[m+1:]
  post.reverse()

  return l[:m] == post


def main():
  print sum([i for i in range(1000000) if is_palindrome(i) and is_palindrome(int(bin(i)[2:]))])


if __name__ == '__main__':
  main()
