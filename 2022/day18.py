#!/usr/bin/env python3

def parse(f):
    space = {}
    for line in f:
        line = line.strip()
        coordinates = tuple(map(int, line.split(",")))
        space[coordinates] = 1
    return space

def neighbours(x, y, z):
    yield (x-1, y, z)
    yield (x+1, y, z)
    yield (x, y-1, z)
    yield (x, y+1, z)
    yield (x, y, z-1)
    yield (x, y, z+1)
   
def solution1(data):
    ans = 0
    for x, y, z in data.keys():
        ans += 6
        for a, b, c in neighbours(x, y, z):
            if (a, b, c) in data:
                ans -= 1
    return ans

def generate_check_surfaces(cube):
    x, y, z, s = cube
    #top
    if s == 0:
        #north
        yield (x, y+1, z+1, 2), (x, y+1, z, 0), (x, y, z, 4)
        #west
        yield x-1, y, z+1, 1
        yield x-1, y, z, 0
        yield x, y, z, 3
        #east
        #south

def process(cube, data):
    ans = []
    for c in generate_check_surfaces(cube):
        s1, s2, s3 = c
       
        if s1[:3] in data:
            ans.append(s1)
        elif s2[:2] in data:
            ans.append(s2)
        else:
            ans.append(s3)
    return ans
    
def process_top(cube, data):
    return []
    ans = []
    x, y, z, s = cube
    if (x-1, y, z-1) in data:
        ans.append((x-1, y, z-1, 1))
    elif (x-1, y, z) in data:
        ans.append((x-1, y, z, 5))
    else:
        ans.append((x, y, z, 3))
    return ans

processes = [process_top, process_east, process_south, process_west, process_north, process_down]

def solution2(data):
    for k in data:
        tmp = k
        break
    x, y, z = tmp
    while z > 0:
        if (x, y, z) in data:
            starting_cube = (x, y, z, 5)
        z -= 1

    queue = [starting_cube]
    resolved = []
    ans = 0

    while len(queue) > 0:
        cube = queue.pop()
        ans += 1
        resolved.append(cube)

        tmp = processes[cube[3]](cube, data)
        for t in tmp:
            if t not in resolved:
                queue.append(t)
    return ans
if __name__ == "__main__":
    with open("day18.txt") as f:
        data = parse(f)
    print(solution1(data))
    print(solution2(data))
