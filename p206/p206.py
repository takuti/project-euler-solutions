# coding: utf-8

def main():
  n = 1000000000
  while True:
    if str(n ** 2)[::2] == '1234567890': break
    n += 1
  print n

if __name__ == '__main__':
  main()
