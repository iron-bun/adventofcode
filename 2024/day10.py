#!/usr/bin/env python3


with open("day10.txt") as f:
  data = {}
  starts = []
  for i, line in enumerate(f):
    line = line.strip()
    for j, char in enumerate(line):
      if char == ".":
        continue
      data[j, i] = int(char)
      if char == "0":
        starts.append((j,i))

directions = ((-1,0), (0,1), (1,0), (0, -1))
ans_1 = 0
ans_2 = 0

for start in starts:
  path = [start]
  destinations = set()
  while len(path) > 0:
    pos = path.pop(0)
    if data.get(pos) == 9:
      destinations.add(pos)
      ans_2 += 1
      continue

    for direction in directions:
      tmp = tuple(map(sum,zip(direction,pos)))
      if 0 <= tmp[0] <= j and 0 <= tmp[1] <= i and data.get(tmp, -1) == data[pos] + 1:
        path.append(tmp)
  ans_1 += len(destinations)
print(ans_1)
print(ans_2)
