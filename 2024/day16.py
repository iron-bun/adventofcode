#!/usr/bin/env python3

layout = {}
start = None
end = None
with open("day16.txt") as f:
    for y, line in enumerate(f):
        line = line.strip()
        for x, char in enumerate(line):
            if char == "S":
                start = (x,y)
                char = "."
            if char == "E":
                end = (x, y)
                char = "."
            layout[x,y] = char

directions = {0:(1,0), 1:(0,1), 2:(-1,0), 3:(0,-1)}
queue = [(0, start, 0,set())]
resolved = {}

while len(queue) > 0:
    queue = sorted(queue, key=lambda x: x[0])
    cost, location, direction, path = queue.pop(0)

    if location == end:
        print(cost)
        print(len(path)+1)
        break
    
    if layout[location] == "#":
        continue

    if (location,direction) in resolved:
        tmp_cost, tmp_path = resolved[location, direction]
        if tmp_cost == cost:
            #there's another way to get here for the same cost
            #merge this route into that one and abandon this one
            for p in path:
              tmp_path.add(p)
        continue

    path = path.copy()
    path.add(location)
    resolved[location,direction] = (cost, path)

    queue.append((cost+1, tuple(map(sum,zip(location, directions[direction]))), direction, path))
    queue.append((cost+1000, location, (direction+1)%4, path))
    queue.append((cost+1000, location, (direction-1)%4, path))
