#!/usr/bin/env python3

from functools import reduce

test_data = ["...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#....."]

def expand_universe(data, scale):
  scale -= 1
  gaps = reduce(lambda x,y: "".join(i if i == "#" else j for i,j in zip(x, y)), data)

  y=0
  for line in data:
    line = line.strip()
    x = 0
    y += 1
    if "#" not in line:
      y += scale
      continue
    for galaxy, gap in zip(line,gaps):
      x += 1
      if gap == ".":
        x+=scale
      elif galaxy == "#":
        yield x, y

galaxies = []
total = 0
with open("day11.txt") as data:
  data = data.readlines()
  for value in expand_universe(data, 2):
    for galaxy in galaxies:
      tmp = abs(value[0]-galaxy[0]) + abs(value[1]-galaxy[1])
      total += tmp
    galaxies.append(value)
print(total)

galaxies = []
total = 0
with open("day11.txt") as data:
  data = data.readlines()
  for value in expand_universe(data, 1_000_000):
    for galaxy in galaxies:
      tmp = abs(value[0]-galaxy[0]) + abs(value[1]-galaxy[1])
      total += tmp
    galaxies.append(value)
print(total)
