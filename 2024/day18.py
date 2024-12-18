#!/usr/bin/env python3

from queue import PriorityQueue
import os

layout = {}

x, y = 70,70
with open("day18.txt") as f:
    for _ in range(1024):
        line = f.readline()
        tmp_x, tmp_y = line.split(",")
        tmp_x, tmp_y = int(tmp_x), int(tmp_y)

        layout[tmp_x, tmp_y] = "#"

def flatten_path(p):
    tmp_path = []
    while p != None:
        tmp_path.append(p[0])
        p = p[1]
    return tmp_path

def print_layout(path=None):
    tmp_path = flatten_path(path)
    for i in range(y+1):
        for j in range(x+1):
            if (j,i) in tmp_path:
                print("o", end="")
            else:
                print(layout.get((j,i),"."), end="")
        print()
    print()

start = (0,0)
end = (x,y)
directions = ((-1,0), (0,-1), (1,0), (0,1))

def solve(l):
    queue = PriorityQueue()
    queue.put((0,start,[start,None]))
    resolved = []
    
    while not queue.empty():
        cost, space, path = queue.get()
        if space in resolved:
            continue
    
        if space == end:
            return cost, path
            
        resolved.append(space)
    
        for d in directions:
            tmp_space = tuple(map(sum, zip(space, d)))
            if 0 <= tmp_space[0] <= x and 0 <= tmp_space[1] <= y and l.get(tmp_space) == None and tmp_space not in resolved:
                queue.put((cost+1, tmp_space, [tmp_space,path]))
    return None, None

print(solve(layout)[0])

with open("day18.txt") as f:
    layout = {}

    for _ in range(1024):
        line = f.readline()
        tmp_x, tmp_y = line.split(",")
        tmp_x, tmp_y = int(tmp_x), int(tmp_y)

        layout[tmp_x, tmp_y] = "#"
        
    ans, path = solve(layout)
    path = flatten_path(path)
        
    for line in f:
        tmp_x, tmp_y = line.split(",")
        tmp_x, tmp_y = int(tmp_x), int(tmp_y)

        layout[tmp_x, tmp_y] = "#"
        
        if (tmp_x, tmp_y) in path:
            ans, path = solve(layout)
            if ans == None:
                break
            path = flatten_path(path)
print(",".join((str(tmp_x), str(tmp_y))))
