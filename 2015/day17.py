#!/usr/bin/env python3

import itertools

containers = []
with open("data/day17.txt") as f:
  for line in f:
    containers.append(int(line))

ans = 0
ans2 = 0
shortest_combo = None
for i in range(len(containers)):
  for combination in itertools.combinations(containers, i):
    if sum(combination) == 150:
      if shortest_combo == None:
        shortest_combo = i
      if i == shortest_combo:
        ans2 += 1
      ans += 1
print(ans)
print(ans2)
