# coding: utf-8

def main():
  cipher = map(int, open('p059_cipher.txt').read().rstrip().split(','))
  max_words = 0 # correct decryption may generate the most words
  key_ans = ''
  raw_ans = ''
  for k1 in range(ord('a'), ord('z')+1):
    for k2 in range(ord('a'), ord('z')+1):
      for k3 in range(ord('a'), ord('z')+1):
        key = chr(k1) + chr(k2) + chr(k3)
        raw = ''
        i = 0
        for c in cipher:
          raw += chr(c^ord(key[i]))
          i = 0 if i == 2 else i + 1
        words = raw.split(' ') # English sentences (the original message) should have spaces.
        l = len(words)
        if l > max_words:
          key_ans = key
          raw_ans = raw
          max_words = l
  # compute the sum of the ASCII values in the original text
  print sum(map(ord, raw_ans))

if __name__ == '__main__':
  main()
