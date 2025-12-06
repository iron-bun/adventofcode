#!/usr/bin/env python3
with open("data/day18.txt") as f:
  layout = {}
  for y, line in enumerate(f.readlines()):
    line = line.strip()
    for x, char in enumerate(line):
      layout[x, y] = char
x+=1
y+=1

def evolve(layout, len_x, len_y, part2):
  offsets = ((-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1,1))

  if part2:
    layout[0,0] = "#"
    layout[x-1,0] = "#"
    layout[0,y-1] = "#"
    layout[x-1,y-1] = "#"
  new_layout = layout

  for _ in range(100):
    layout = new_layout
    new_layout = {}
    for i in range(x):
      for j in range(y):
        tmp = 0
        for offset in offsets:
          if layout.get(tuple(map(lambda a: a[0]+a[1], zip(offset, (i, j)))), ".") == "#":
            tmp += 1
        if layout[i,j] == "#" and tmp in (2,3):
          new_layout[i, j] = "#"
        elif layout[i,j] == "." and tmp == 3:
          new_layout[i, j] = "#"
        else:
          new_layout[i, j] = "."

    if part2:
      new_layout[0,0] = "#"
      new_layout[x-1,0] = "#"
      new_layout[0,y-1] = "#"
      new_layout[x-1,y-1] = "#"
  return new_layout

new_layout = evolve(layout, x, y, False)
ans = 0
for i in range(x):
  for j in range(y):
    if new_layout[i, j] == "#":
      ans += 1
print(ans)

new_layout = evolve(layout, x, y, True)
ans = 0
for i in range(x):
  for j in range(y):
    if new_layout[i, j] == "#":
      ans += 1
print(ans)
