# coding: utf-8

def main():
  w1 = map(len, 'one two three four five six seven eight nine'.split())
  w10s = map(len, 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())
  cnt = sum(w1) + sum(w10s)

  w_ty = map(lambda n: len(n)+2, 'twen thir for fif six seven eigh nine'.split())
  w20to99 = []
  for i in range(20, 100):
    d10, d1 = map(int, str(i))
    cnt_d1 = w1[d1-1] if d1 !=0 else 0
    w20to99.append(w_ty[d10-2] + cnt_d1)
  cnt += sum(w20to99)

  h = len('hundred')
  a = len('and')
  w100to999 = []
  for i in range(100, 1000):
    d100, d10, d1 = map(int, str(i))
    if d10 == 0: cnt_d10 = (a + w1[d1-1]) if d1 != 0 else 0
    elif d10 == 1: cnt_d10 = a + w10s[d1]
    else: cnt_d10 = a + w20to99[int('%d%d' % (d10,d1))-20]
    w100to999.append(w1[d100-1] + h + cnt_d10)
  cnt += sum(w100to999)

  cnt += len('onethousand')
  print cnt


if __name__ == '__main__':
  main()
