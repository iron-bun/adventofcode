#!/usr/bin/env python3

from math import copysign

testdata = ["7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"]

def check(line):
    s = None
    for a, b in zip(line, line[1:]):
      tmp = a-b
      if s == None:
        s = copysign(1, tmp)
      if copysign(1, tmp) != s:
        break
      if abs(tmp) < 1 or abs(tmp) > 3:
        break
    else:
      return True
    return False

ans = 0 
with open("./day02.txt") as f:
  for line in f:
    line = line.strip().split()
    line = list(map(int, line))

    if check(line):
      ans += 1
print(ans)

ans = 0
with open("./day02.txt") as f:
  for line in f:
    line = line.strip().split()
    line = list(map(int, line))

    if check(line):
      ans += 1
    else:
      for idx in range(len(line)):
        tmp = line[:]
        del tmp[idx]
        if check(tmp):
          ans += 1
          break

print(ans)
