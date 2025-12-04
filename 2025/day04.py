#!/usr/bin/env python3

layout = {}
with open("day04.txt") as f:
  for i, line in enumerate(f):
      for j, char in enumerate(line.strip()):
          layout[j, i] = char

offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

ans = 0
for x in range(i+1):
    for y in range(j+1):
        if layout.get((x, y)) == ".":
            continue
        tmp = 0
        for offset in offsets:
            if layout.get(tuple(map(lambda a: a[0]+a[1], zip(offset, (x, y)))), ".") == "@":
                tmp += 1
        if tmp < 4:
            ans += 1
print(ans)

ans = 0
queue = set([(x, y) for x in range(i+1) for y in range(j+1)])
while len(queue) > 0:
    location = queue.pop()
    if layout.get(location, ".") == ".":
        continue

    tmp = 0
    tmp_offsets = []
    for offset in offsets:
        tmp_offsets.append(tuple(map(lambda a: a[0]+a[1], zip(offset, location))))
        if layout.get(tmp_offsets[-1], ".") == "@":
            tmp += 1
    if tmp < 4:
        ans += 1
        queue = queue.union(set(tmp_offsets))
        layout[location] = "."
print(ans)
