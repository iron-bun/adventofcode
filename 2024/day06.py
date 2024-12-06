#!/usr/bin/env python3

map_data = {}
start = None
pos = None

with open("day06.txt") as f:
  for i, line in enumerate(f):
    line = line.strip()
    for j, char in enumerate(line):
      if char == "^":
        start = (j, i)
        pos = start
        char = "X"
      map_data[j,i] = char

directions = ((0,-1),(1,0),(0,1),(-1,0))
didx = 0

data = map_data.copy()
while data.get(pos) != None:
  data[pos] = "X"

  tmp = tuple(map(sum,zip(pos, directions[didx])))
  if data.get(tmp) == "#":
    didx += 1
    didx %= 4

  pos = tuple(map(sum,zip(pos, directions[didx])))

print(sum(1 for v in data.values() if v == "X"))

ans = 0
for y in range(i+1):
  for x in range(j+1):
    if (x, y) == start or data[x,y] != "X":
      continue

    tmp = map_data.copy()
    tmp[x, y] = "#"
    pos = start
    didx = 0

    while tmp.get(pos) != None and tmp.get(pos) != didx:
      tmp[pos] = didx
      ptmp = tuple(map(sum,zip(pos, directions[didx])))
      while tmp.get(ptmp) == "#":
        didx += 1
        didx %= 4
        ptmp = tuple(map(sum,zip(pos, directions[didx])))
      pos = tuple(map(sum,zip(pos, directions[didx])))
    if tmp.get(pos) != None:
      ans += 1
print(ans)

