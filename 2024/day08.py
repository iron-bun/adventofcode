#!/usr/bin/env python3

maps = {}
with open("day08.txt") as f:
  for i, line in enumerate(f):
    for j, char in enumerate(line.strip()):
      if char == ".":
        continue
      tmp = maps.get(char, [])
      tmp.append((i,j))
      maps[char] = tmp

antinodes = set()
for k in maps:
  for idx, antenna in enumerate(maps[k]):
    for other_antenna in maps[k]:
      if antenna == other_antenna:
        continue
      tmp = tuple(map(lambda x: x[0]-x[1],zip(antenna, other_antenna)))
      node = tuple(map(lambda x: x[0]-x[1],zip(other_antenna, tmp)))
      
      if (0 <= node[0] <= i and 0 <= node[1] <= j):
        antinodes.add(node)
print(len(antinodes))

antinodes = set()
for k in maps:
  for idx, antenna in enumerate(maps[k]):
    for other_antenna in maps[k]:
      if antenna == other_antenna:
        continue
      antinodes.add(antenna)
      tmp = tuple(map(lambda x: x[0]-x[1],zip(antenna, other_antenna)))
      node = tuple(map(lambda x: x[0]-x[1],zip(other_antenna, tmp)))
      while (0 <= node[0] <= i and 0 <= node[1] <= j):
        antinodes.add(node)
        node = tuple(map(lambda x: x[0]-x[1],zip(node, tmp)))
print(len(antinodes))

