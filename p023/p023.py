# coding: utf-8

def proper_divisors(n):
  upper = (n / 2) if n % 2 == 0 else (n / 3)
  divisors = []
  for i in range(1, upper+1):
    if n % i == 0: divisors.append(i)
  return divisors

def all_possible_sum(numbers):
  """ return all pissible sums
  """
  s = []
  n = len(numbers)
  for i in range(n):
    for j in range(n):
      s.append(numbers[i] + numbers[j])
  return s

def is_in(a, n):
  """ find n from sorted-array a
  """
  l = 0
  r = len(a) - 1
  while l <= r:
    mid = (l + r) / 2
    if n == a[mid]: return True
    elif n > a[mid]: l = mid + 1
    else: r = mid - 1
  return False

def main():
  upper_limit = 28123

  # find all abundant numbers
  abundants = []
  for i in range(1, upper_limit+1):
    if sum(proper_divisors(i)) > i: abundants.append(i)

  sums = all_possible_sum(abundants)
  sums.sort()

  # for each number below the upper-limit,
  # check wheather the number cannot be written as the sum of 2 abundants.
  total = 0
  for i in range(1, upper_limit+1):
    if not is_in(sums, i): total += i
  print 'The sum of all the positive integers which cannot be written as the sum of two abundant numbers :', total


if __name__ == '__main__':
  main()
