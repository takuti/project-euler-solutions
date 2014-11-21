def factorial(n):
  ans = 1
  for i in range(2, n+1):
    ans *= i
  return ans

print sum([ int(c) for c in str(factorial(100))])
