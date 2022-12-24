#!/usr/bin/env python3

def parse(f):
    space = []
    for line in f:
        line = line.strip()
        coordinates = tuple(map(int, line.split(",")))
        space.append(coordinates)
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
    for x, y, z in data:
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
        yield (x-1, y, z+1, 1), (x-1, y, z, 0), (x, y, z, 3)
        #east
        yield (x+1, y, z+1, 3), (x+1, y, z, 0), (x, y, z, 1) 
        #south
        yield (x, y-1, z+1, 4), (x, y-1, z, 0), (x, y, z, 2)
    if s == 1:
        #top
        yield (x+1, y, z+1, 5), (x, y, z+1, 1), (x, y, z, 0)
        #bottom
        yield (x+1, y, z-1, 0), (x, y, z-1, 1), (x, y, z, 5)
        #north
        yield (x+1, y+1, z, 2), (x, y+1, z, 1), (x, y, z, 4)
        #south
        yield (x+1, y-1, z, 4), (x, y-1, z, 1), (x, y, z, 2)
    if s == 2:
        #top
        yield (x, y-1, z+1, 5), (x, y, z+1, 2), (x, y, z, 0)
        #bottom
        yield (x, y-1, z-1, 0), (x, y, z-1, 2), (x, y, z, 5)
        #east
        yield (x+1, y-1, z, 3), (x+1, y, z, 2), (x, y, z, 1)
        #west
        yield (x-1, y-1, z, 1), (x-1, y, z, 2), (x, y, z, 3)
    if s == 3:
        #top
        yield (x-1, y, z+1, 5), (x, y, z+1, 3), (x, y, z, 0)
        #bottom
        yield (x-1, y, z-1, 0), (x, y, z-1, 3), (x, y, z, 5)
        #north
        yield (x-1, y+1, z, 2), (x, y+1, z, 3), (x, y, z, 4)
        #south
        yield (x-1, y-1, z, 4), (x, y-1, z, 3), (x, y, z, 2)
    if s == 4:
        #top
        yield (x, y+1, z+1, 5), (x, y, z+1, 4), (x, y, z, 0)
        #bottom
        yield (x, y+1, z-1, 0), (x, y, z-1, 4), (x, y, z, 5)
        #east
        yield (x+1, y+1, z, 3), (x+1, y, z, 4), (x, y, z, 1)
        #west
        yield (x-1, y+1, z, 1), (x-1, y, z, 4), (x, y, z, 3)
    if s == 5:
        #north
        yield (x, y+1, z-1, 2), (x, y+1, z, 5), (x, y, z, 4)
        #south
        yield (x, y-1, z-1, 4), (x, y-1, z, 5), (x, y, z, 2)
        #east
        yield (x+1, y, z-1, 3), (x+1, y, z, 5), (x, y, z, 1)
        #west
        yield (x-1, y, z-1, 1), (x-1, y, z, 5), (x, y, z, 3)
    return

def process(cube, data):
    ans = []
    for c in generate_check_surfaces(cube):
        s1, s2, s3 = c
       
        if s1[:3] in data:
            ans.append(s1)
        elif s2[:3] in data:
            ans.append(s2)
        else:
            ans.append(s3)
    return ans
    
def solution2(data):
    resolved = set()
    for k in data:
            
        x, y, z = k
        while z > 0:
            if (x, y, z) in data:
                starting_cube = (x, y, z, 5)
            z -= 1
    
        queue = [starting_cube]
    
        while len(queue) > 0:
            cube = queue.pop()
            if cube in resolved:
                continue
            print(cube)
            resolved.add(cube)
    
            for t in process(cube, data):
                if t not in resolved:
                    queue.append(t)
    return len(resolved)
    
if __name__ == "__main__":
    with open("day18.txt") as f:
        data = parse(f)
    print(solution1(data))
    print(solution2(data))
    
