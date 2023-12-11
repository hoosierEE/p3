# https://www.lintcode.com/problem/659/
# encode/decode list of strings

def enc(lst):
 i = ' '.join(str(len(x)) for x in lst)+'  '
 s = ''.join(lst)
 return i+s

def dec(s):
 cuts = [int(x) for x in s[:s.index('  ')].split(' ')]
 st = s[s.index('  ')+2:]
 ls = []
 for c in cuts:
  ls.append(st[:c])
  st = st[c:]
 return ls


if __name__ == "__main__":
 tests = [
  [''],
  [' '],
  ['  '],
  ['aaa'],
  ['aa a ',' ',' b bb b ', 'b'],
  ['hello','hi','world'],
  ['helloooooooooooooooooooooooooooooooooooo','hi','world'],
 ]

 for t in tests:
  print(repr(enc(t)))
  assert t == dec(enc(t))
