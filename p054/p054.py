# coding: utf-8

cards = map(str, range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']

def is_subarray(a, s):
  """ whether s is a subarray of array a
  >>> is_subarray([1, 2, 3, 5], [1, 2])
  True
  >>> is_subarray([1, 2, 3, 5], [1, 3])
  False
  """
  len_a = len(a)
  len_s = len(s)
  if len_s > len_a: return False
  for i in range(len_a - len_s):
    if a[i:i+len_s] == s: return True
  return False

def rank(hand):
  """
  (rank, value)
  value = -1 if the rank is based on suits
  """
  hand.sort(key=lambda h: cards.index(h[0]))
  values = [c[0] for c in hand]
  suits = [c[1] for c in hand]

  if values == ['T', 'J', 'Q', 'K', 'A']: return (9, -1) # royal flush

  ss = list(set(suits))
  if len(ss) == 1 and is_subarray(cards, values): return (8, -1) # straight flush

  sv = list(set(values))
  if len(sv) == 2:
    # four of a kind
    if values.count(sv[0]) == 4:
      return (7, sv[0])
    elif values.count(sv[1]) == 4:
      return (7, sv[1])
    # full house
    if values.count(sv[0]) == 3:
      return (6, sv[0])
    elif values.count(sv[1]) == 3:
      return (6, sv[1])

  if len(ss) == 1: return (5, -1) # flush
  if is_subarray(cards, values): return (4, -1) # straight
  if len(sv) == 3:
    # three of a kind
    if values.count(sv[0]) == 3:
      return (3, sv[0])
    elif values.count(sv[1]) == 3:
      return (3, sv[1])
    elif values.count(sv[2]) == 3:
      return (3, sv[2])
    # two pairs
    if values.count(sv[0]) == 2 and values.count(sv[1]) == 2:
      return (2, sv[0])
    elif values.count(sv[1]) == 2 and values.count(sv[2]) == 2:
      return (2, sv[1])
    elif values.count(sv[2]) == 2 and values.count(sv[0]) == 2:
      return (2, sv[2])
  if len(sv) == 4:
    # one pair
    if values.count(sv[0]) == 2:
      return (1, sv[0])
    elif values.count(sv[1]) == 2:
      return (1, sv[1])
    elif values.count(sv[2]) == 2:
      return (1, sv[2])
    elif values.count(sv[3]) == 2:
      return (1, sv[2])
  return (0, -1)

def judge(p1, p2):
  """ compare two hands (p1 and p2), and return which one wins
  >>> judge(['5H', '5C', '6S', '7S', 'KD'], ['2C', '3S', '8S', '8D', 'TD'])
  2
  >>> judge(['5D', '8C', '9S', 'JS', 'AC'], ['2C', '5C', '7D', '8S', 'QH'])
  1
  >>> judge(['2D', '9C', 'AS', 'AH', 'AC'], ['3D', '6D', '7D', 'TD', 'QD'])
  2
  >>> judge(['4D', '6S', '9H', 'QH', 'QC'], ['3D', '6D', '7H', 'QD', 'QS'])
  1
  >>> judge(['2H', '2D', '4C', '4D', '4S'], ['3C', '3D', '3S', '9S', '9D'])
  1
  """
  r1, v1 = rank(p1)
  r2, v2 = rank(p2)
  if r1 > r2: return 1
  elif r1 < r2: return 2
  else:
    if v1 > v2: return 1
    elif v1 < v2: return 2
    else:
      s1 = sorted([cards.index(c[0]) for c in p1], reverse=True)
      s2 = sorted([cards.index(c[0]) for c in p2], reverse=True)
      for i in range(5):
        if s1[i] > s2[i]: return 1
        elif s1[i] < s2[i]: return 2

def main():
  cnt = 0
  for hands in map(lambda l: l.rstrip().split(' '), open('p054_poker.txt').readlines()):
    p1 = hands[:5]
    p2 = hands[5:]
    if judge(p1, p2) == 1: cnt += 1
  print cnt

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
