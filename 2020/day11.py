#!/usr/bin/env python3

def get_surround(x, y, data):
    surround = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0,0):
                continue
            surround.append(data.get((x+i, y+j), "."))
    return surround

def get_project(x, y, data):
    surround = []
    directions = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    tmp = 1
    while len(directions) > 0:
        next_directions = []
        for d in directions:
            seat = data.get((x+d[0]*tmp, y+d[1]*tmp))
            if seat == None:
                pass
            elif seat == "#":
                surround.append("#")
            elif seat == "L":
                surround.append("L")
            else:
                next_directions.append(d)
        directions = next_directions
        tmp += 1
    return surround

def evolve(width, height, data, too_crowded, find_surround):
    new_data = {}
    for x in range(width):
        for y in range(height):
            seat = data[x, y]
            if seat == ".":
                new_data[x, y] = seat
                continue
            surround = find_surround(x, y, data)
            tmp = sum([1 for v in surround if v == "#"])

            if tmp == 0:
                new_data[x, y] = "#"
            elif tmp >= too_crowded:
                new_data[x, y] = "L"
            else:
                new_data[x, y] = seat

    return new_data

def solution(f, too_crowded, find_surround):
    data = {}
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
             data[x, y] = char
    width, height = x+1, y+1

    prev = {}

    while prev != data:
        prev = data
        data = evolve(width, height, data, too_crowded, find_surround)

    return sum(1 for v in data.values() if v == "#")



if __name__ == "__main__":
    with open("day11.txt") as f:
        print(solution(f, 4, get_surround))
    with open("day11.txt") as f:
        print(solution(f, 5, get_project))
