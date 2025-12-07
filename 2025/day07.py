#!/usr/bin/env python3

with open("day07.txt") as f:
  manifold = f.readlines()

tachyons = set([manifold[0].index("S")])
ans = 0
for i in range(2,len(manifold),2):
  tmp = set()
  for tachyon in tachyons:
    if manifold[i][tachyon] == "^":
      ans += 1
      tmp.add(tachyon - 1)
      tmp.add(tachyon + 1)
    else:
      tmp.add(tachyon)
  tachyons = tmp
print(ans)

tachyons = {manifold[0].index("S"):1}
for i in range(2,len(manifold),2):
  tmp = {}
  for tachyon in tachyons:
    if manifold[i][tachyon] == "^":
      tmp[tachyon - 1] = tmp.get(tachyon-1, 0) + tachyons[tachyon]
      tmp[tachyon + 1] = tachyons[tachyon]
    else:
      tmp[tachyon] = tmp.get(tachyon,0) + tachyons[tachyon]
  tachyons = tmp
print(sum(tachyons.values()))

