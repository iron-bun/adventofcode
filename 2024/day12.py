#!/usr/bin/env python3

with open("day12.txt") as f:
  data = {}
  for i, line in enumerate(f):
    line = line.strip()
    for j, char in enumerate(line):
      data[j,i] = char

directions = ((-1,0),(0,1),(1,0),(0,-1))
ans_1 = 0
ans_2 = 0

while len(data) > 0:
  k = next(iter(data))
  plant = data[k]
  region = set()
  queue = set()
  queue.add(k)

  fence_set = set()
 
  fences = 0

  while len(queue) > 0:
    k = queue.pop()
    region.add(k)
    for idx,d in enumerate(directions):
      tmp = tuple(map(sum,zip(k, d)))
      if tmp in region:
        continue
      elif data.get(tmp) == plant:
        queue.add(tmp)
      else:
        fences += 1
        tmp2 = k
        tmp3 = tmp
        while data.get(tmp2) == plant and data.get(tmp3) != plant:
          tmp2 = tuple(map(sum,zip(tmp2, directions[(idx+1)%4])))
          tmp3 = tuple(map(sum,zip(tmp3, directions[(idx+1)%4])))
        fence_set.add((tmp2,idx))

  ans_1 += len(region) * fences
  ans_2 += len(region) * len(fence_set)
  for i in region:
    del data[i]

print(ans_1)
print(ans_2)
