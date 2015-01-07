# coding: utf-8

def is_triangle(a, b, c):
  """ c is the longest edge
  >>> is_triangle(20, 48, 52)
  True
  >>> is_triangle(1, 1, 1)
  False
  """
  if a ** 2 + b ** 2 == c ** 2: return True
  else: return False

def count_solutions(p):
  """ Try all possible combinations of {a, b, c}
  >>> count_solutions(120)
  3
  """
  solutions = []
  for a in xrange(1, (p/2-2)+1): # p/2 because {a, b, c} and {c, b, a} are the same triangle
    for b in xrange(1, (p-a-1)+1):
      c = p - (a + b)
      l = sorted([a, b, c])
      if l not in solutions and is_triangle(l[0], l[1], l[2]):
        solutions.append(l)
  return len(solutions)

def main():
  max_cnt = 0
  max_p = 0
  for p in xrange(3, 1001):
    cnt = count_solutions(p)
    if cnt > max_cnt:
      max_cnt = cnt
      max_p = p
  print max_p

if __name__ == '__main__':
  main()
