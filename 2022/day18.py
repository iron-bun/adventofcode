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

if __name__ == "__main__":
    with open("day18.txt") as f:
        data = parse(f)
    print(solution1(data))
