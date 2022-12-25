#!/usr/bin/env python3

def parse(f):
    space = []
    for line in f:
        line = line.strip()
        coordinates = tuple(map(int, line.split(",")))
        space.append(coordinates)
    return space

def neighbours(cube):
    x, y, z = cube
    yield (x-1, y, z)
    yield (x+1, y, z)
    yield (x, y-1, z)
    yield (x, y+1, z)
    yield (x, y, z-1)
    yield (x, y, z+1)

def extra_neighbours(cube):
    yield from neighbours(cube)
    x, y, z = cube
    yield (x-1, y+1, z+1)   
    yield (x+1, y+1, z+1)   
    yield (x-1, y-1, z+1)   
    yield (x+1, y-1, z+1)   
    yield (x-1, y+1, z-1)   
    yield (x+1, y+1, z-1)   
    yield (x-1, y-1, z-1)   
    yield (x+1, y-1, z-1)
    yield (x, y-1, z-1)
    yield (x-1, y, z-1)
    yield (x, y+1, z-1)
    yield (x+1, y, z-1)
    yield (x, y-1, z+1)
    yield (x-1, y, z+1)
    yield (x, y+1, z+1)
    yield (x+1, y, z+1)

def solution1(data):
    ans = 0
    for cube in data:
        ans += 6
        for test_cube in neighbours(cube):
            if test_cube in data:
                ans -= 1
    return ans

def solution2(data):
    for k in data:
        break

    x, y, z = k
    while z > 0:
        if (x, y, z) in data:
            starting_cube = (x, y, z)
        z -= 1
    x, y, z = starting_cube
    queue = [(x,y, z-1)]
    resolved = set()

    while len(queue) > 0:
        cube = queue.pop()
        if cube in resolved:
            continue
        resolved.add(cube)
        for new_cube in neighbours(cube):
            if new_cube in data:
                continue
            if new_cube in resolved:
                continue
            for test_cube in extra_neighbours(new_cube):
                if test_cube in data:
                    queue.append(new_cube)
                    break
    ans = 0
    for cube in resolved:
        for test_cube in neighbours(cube):
            if test_cube in data:
                ans += 1
    return ans

if __name__ == "__main__":
    with open("day18.txt") as f:
        data = parse(f)
    print(solution1(data))
    print(solution2(data))

