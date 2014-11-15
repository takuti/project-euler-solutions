# coding: utf-8

def main():
  print str(sum([i ** i for i in range(1,1000+1)]))[-10:]

if __name__ == '__main__':
  main()
