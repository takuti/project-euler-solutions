n = ''.join(map(str, range(1,1000000)))

ds = map(int, [n[10**i - 1] for i in range(0,7)])
ans = 1
for d in ds:
  ans *= d
print ans
