#!/usr/bin/env python3

from collections import defaultdict

test_data = ["1,0,1~1,2,1",
"0,0,2~2,0,2",
"0,2,3~2,2,3",
"0,0,4~0,2,4",
"2,0,5~2,2,5",
"0,1,6~2,1,6",
"1,1,8~1,1,9"]

class block:
  def __init__(self, name, location):
    self.name = name
    tmp = location.split("~")
    self.loc0 = tuple(map(int, tmp[0].split(",")))
    self.loc1 = tuple(map(int, tmp[1].split(",")))

    self.z = min(self.loc0[2], self.loc1[2])
    self.height = max(self.loc0[2], self.loc1[2]) - self.z + 1

    self.x = min(self.loc0[0], self.loc1[0])
    self.length = max(self.loc0[0], self.loc1[0]) - self.x + 1

    self.y = min(self.loc0[1], self.loc1[1])
    self.width = max(self.loc0[1], self.loc1[1]) - self.y + 1

    self.supports = set()
    self.supported = set()

    self.dc = None

  def single_support(self):

    if len(block.supports) == 0:
      return False

    for s in block.supports:
      if len(s.supported) == 1:
        return True

    return False

  def drop_count(self):
    pass

blocks = {}
with open("day22.txt") as f:
  data = test_data
  data = f
  for idx, line in enumerate(data):
    line = line.strip()
    #blocks[chr(ord("A")+idx)] = block(chr(ord("A")+idx), line)
    blocks[idx] = block(idx, line)

ans = 0
block_names = sorted(blocks.keys(), key=lambda x: blocks[x].z)

floor = {}
for bn in block_names:
  block = blocks[bn]
  supports = defaultdict(list)

  for x in range(block.x, block.x + block.length):
    for y in range(block.y, block.y + block.width):
      z, name = floor.get((x, y), (0, "floor"))
      if z > 0 and name not in [v for values in supports.values() for v in values]:
        supports[z].append(name)

  if len(supports.keys()) > 0:
     z = max(supports.keys())
     for s in supports[z]:
       blocks[s].supports.add(blocks[bn])
       block.supported.add(blocks[s])
  
  for x in range(block.x, block.x + block.length):
    for y in range(block.y, block.y + block.width):
      floor[x, y] = z + block.height, block.name

block_names = sorted(blocks.keys(), key=lambda x: blocks[x].z, reverse=True)
for bn in block_names:
  block = blocks[bn]
  if not block.single_support():
    ans += 1

print(ans)

ans = 0
for bn in block_names:
  block = blocks[bn]
  falling = set()
  tmp = list(block.supports)
  while len(tmp) > 0:
    b = tmp.pop(0)
    if len([s for s in b.supported if s != block and s not in falling]) == 0:
      falling.add(b)
      tmp += list(b.supports)
  pass
  ans += len(falling)

print(ans)

