# coding: utf-8

def main():
  cancelled = []
  for i in range(1, 10):
    for j in range(i+1, 10):
      cancelled.append((str(i),str(j)))

  nume_prod = deno_prod = 1
  for numerator in range(10, 100):
    for denominator in range(numerator+1, 100):
      nume_d = str(numerator)
      deno_d = str(denominator)
      if nume_d[1] == '0' and deno_d[1] == '0': continue # trivial
      o = float(numerator) / denominator
      if nume_d[0] == deno_d[0] and (nume_d[1], deno_d[1]) in cancelled:
        if float(nume_d[1]) / float(deno_d[1]) != o: continue
      elif nume_d[0] == deno_d[1] and (nume_d[1], deno_d[0]) in cancelled:
        if float(nume_d[1]) / float(deno_d[0]) != o: continue
      elif nume_d[1] == deno_d[0] and (nume_d[0], deno_d[1]) in cancelled:
        if float(nume_d[0]) / float(deno_d[1]) != o: continue
      elif nume_d[1] == deno_d[1] and (nume_d[0], deno_d[0]) in cancelled:
        if float(nume_d[0]) / float(deno_d[0]) != o: continue
      else: continue
      print numerator, denominator
      nume_prod *= numerator
      deno_prod *= denominator
  print nume_prod, deno_prod

if __name__ == '__main__':
  main()
