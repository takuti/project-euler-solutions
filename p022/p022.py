# coding: utf-8

def read_names():
  f = open('p022_names.txt')
  names = f.read()
  return names.replace('\"','').split(',')

def alpha_score(name):
  """ Compute a score of the given name based on its alphabetical position
  >>> alpha_score('COLIN')
  53
  """
  return sum(map(lambda c: (ord(c)-ord('A')+1), name))

def main():
  names = read_names()
  names.sort()
  total = 0
  for n in names:
    total += alpha_score(n) * (names.index(n) + 1)
  print total

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
