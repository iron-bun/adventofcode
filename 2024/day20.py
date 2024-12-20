#!/usr/bin/env python3

from queue import PriorityQueue

with open("day20.txt") as f:
    layout = {}
    start = None
    end = None
    for y,line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "S":
                start = (x,y)
                char = "."
            if char == "E":
                end = (x,y)
                char = "."
            layout[x,y] = char

queue = PriorityQueue()
queue.put((0, start))
costs = {}
directions = ((1,0), (0, 1), (-1, 0), (0, -1))

while not queue.empty():
    cost, space = queue.get()

    if space in costs:
        continue

    costs[space] = cost

    if space == end:
        break
    
    for d in directions:
        tmp = tuple(map(sum, zip(space, d)))
        if layout.get(tmp) == ".":
            queue.put((cost+1, tmp))

skips_1, skips_2 = {}, {}
for k1 in costs:
    for i in range(-20, 21):
        if k1[0] + i < 0 or k1[0] + i > x:
            continue
        for j in range(-20-i, 21-i):
            if k1[1] + j < 0 or k1[1]+j > y:
                continue
            
            if i == 0 and j == 0:
                continue

            k2 = (k1[0]+i, k1[1]+j)
            if costs.get(k2) == None or costs[k1] >= costs[k2]:
                continue
        
            dist = abs(k1[0] - k2[0]) + abs(k1[1] - k2[1])
            saving = costs[k2] - costs[k1] - dist
        
            if saving <= 0:
                continue
            if dist <= 20:
                skips_2[saving] = skips_2.get(saving, 0) + 1
            if dist <= 2:
                skips_1[saving] = skips_1.get(saving, 0) + 1

ans = 0
for k in sorted(skips_1.keys()):
    if k >= 100:
        ans += skips_1[k]
print(ans)

ans = 0
for k in sorted(skips_2.keys()):
    if k >= 100:
        ans += skips_2[k]
print(ans)
