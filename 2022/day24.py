#!/usr/bin/env python3

from queue import PriorityQueue

def parse(f):
    data = {}
    tmp = 0
    for y, line in enumerate(f):
        tmp += 1
        line = line.strip()
        for x, value in enumerate(line):
            if value != ".":
                if (x, y) not in data:
                    data[(x, y)] = []
                data[x, y].append(value)
    data[(1, -1)] = "#"
    data[(line.index("."), tmp)] = "#"
    return data, line.index("."), tmp-1

def get_neighbours(t, x, y, data):
    if (x, y) not in data:
        yield t, x, y
    if (x-1, y) not in data:
        yield t, x-1, y
    if (x+1, y) not in data:
        yield t, x+1, y
    if (x, y-1) not in data:
        yield t, x, y-1
    if (x, y+1) not in data:
        yield t, x, y+1

def evolve(data, loop_x, loop_y):
    new_data = {}
    for k, values in data.items():
        for v in values:
            x, y = k
            if v == ">":
                x += 1
                if data.get((x, y), None) == ["#"]:
                    x = 1

            if v == "<":
                x -= 1
                if data.get((x, y), None) == ["#"]:
                    x = loop_x

            if v == "v":
                y += 1
                if data.get((x, y), None) == ["#"]:
                    y = 1

            if v == "^":
                y -= 1
                if data.get((x, y), None) == ["#"]:
                    y = loop_y

            if (x, y) not in new_data:
                new_data[x, y] = []
            new_data[x, y].append(v)
    return new_data

def print_map(new_data):
    for j in range(10):
        for i in range(10):
            if (i, j) not in new_data:
                print(" ", end="")
            elif len(new_data[(i, j)]) == 1:
                print(new_data[(i,j)][0], end="")
            else:
                print(len(new_data[i,j]), end="")
        print()

def solution(data, goals):
    maps = {}
    maps[0] = data
    #queue = PriorityQueue()
    #queue.put((0,0,1,0, [0]))
    queue = set()
    queue.add((0,0,1,0,goals))
    loop_x, loop_y = goals[0][0],goals[0][1]
    resolved = []

    min_time = None
    while not len(queue) == 0:
        tmp = sorted(list(queue), key=lambda x: x[0], reverse=True)
        score, t, x, y, g = tmp.pop()
        queue.remove((score, t, x, y, g))
        #print(score, t, x, y, g)

        if (x, y) != g[0]:
            goal = g[0]
        elif len(g) > 1:
            g = g[1:]
            goal = g[0]
            queue = set()
        elif (min_time == None or min_time > t):
            return t

        resolved.append((t, x, y))

        if t+1 not in maps:
            maps[t+1] = evolve(maps[t], loop_x, loop_y-1)

        for t1, x1, y1 in get_neighbours(t+1, x, y, maps[t+1]):
            s1 = abs(goal[0]-x1)*100 + abs(goal[1]-y1)*100 + t1*50
            if (t1, x1, y1) not in resolved:
                tmp.append((x, y))
                queue.add((s1, t1, x1, y1, g))
        
    return min_time

if __name__ == "__main__":
    with open("day24.txt") as f:
        data, gx, gy = parse(f)
    print_map(data)
    print(solution(data, ((gx, gy), )))
    print(solution(data, ((gx, gy), (1,0), (gx,gy))))
