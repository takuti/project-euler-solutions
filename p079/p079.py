# coding: utf-8

def check_attemps(passcode, logs):
  for log in logs:
    j = 0
    for i in range(3):
      if log[i] in passcode[j:]:
        j += passcode[j:].index(log[i]) + 1
      else:
        return False
  return True

def main():
  logs = map(lambda l: l.rstrip(), open('p079_keylog.txt').readlines())
  passcode = 0
  while not check_attemps(str(passcode), logs):
    passcode += 1
  print passcode

if __name__ == '__main__':
  main()

