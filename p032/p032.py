# coding: utf-8

def is_pandigital(sn):
  l = list(sn)
  if min(l) != '1': return False
  uniq_len = len(set(l))
  if len(l) != uniq_len: return False
  if uniq_len != int(max(l)): return False
  return True

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
  products = []
  a = 2
  while True:
    sa = str(a)
    a_len = len(sa)
    if a_len + 1 + len(str(a*1)) > 9: break
    b = 2
    while True:
      sb = str(b)
      p = a * b
      sp = str(p)
      total_len = a_len + len(sb) + len(sp)
      if total_len > 9: break
      if total_len == 9 and is_pandigital(sa + sb + sp):
        if not is_in(products, p):
          products.append(p)
          products.sort()
      b += 1
    a += 1
  print sum(products)



if __name__ == '__main__':
  main()
