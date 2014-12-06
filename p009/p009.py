# coding: utf-8

""" Find one Pythagorean triplet for which a + b + c = 1000
"""

def main():
  flg = False
  # a + (a+1) + (a+2) < 1000
  for a in range(1, 1000/3 + 1):
    if flg: break
    # b + (b+1) < 1000 - a
    for b in range(a+1, (1000-a-1)/2 + 1):
      if flg: break
      c = 1000 - a - b
      if a ** 2 + b ** 2 == c ** 2:
        print a * b * c
        flg = True


if __name__ == '__main__':
  main()
