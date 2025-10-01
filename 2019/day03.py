#!/usr/bin/env python3

from operator import add

def parse_line(line):
    grid = {}
    paths = line.split(",")

    location = (0,0)

    directions = {"R": (1,0), "D": (0,-1), "L": (-1,0), "U": (0,1)}
    length = 0
    for p in paths:
        direction = p[0]
        steps = int(p[1:])

        for _ in range(steps):
          length += 1
          location = tuple(map(lambda x: x[0]+x[1], zip(location, directions[direction])))

          if location not in grid:
              grid[location] = length
    return grid

with open("day03.txt") as f:
  path1 = parse_line(f.readline())
  path2 = parse_line(f.readline())

ans = None
intersections = set(path1.keys()).intersection(path2.keys())

for i in intersections:
    tmp = abs(i[0]) + abs(i[1])
    if ans == None or ans > tmp:
      ans = tmp
print(ans)

ans = None
for i in intersections:
    tmp = path1[i] + path2[i]
    if ans == None or tmp < ans:
        ans = tmp
print(ans)
