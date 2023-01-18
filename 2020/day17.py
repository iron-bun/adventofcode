#!/usr/bin/env python3


def get_3d_neighbours(x, y, z):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (i, j, k) == (0, 0, 0):
                    continue
                yield x+i, y+j, z+k

def get_4d_neighbours(x, y, z, w):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (i, j, k, l) == (0, 0, 0, 0):
                        continue
                    yield x+i, y+j, z+k, w+l

def solution1(f):

    cells = set()
    z = 0
    for y, line in enumerate(f):
        for x, value in enumerate(line.strip()):
            if value == "#":
                cells.add((x, y, z))

    for _ in range(6):
        check_area = set()
        new_cells = set()

        for x, y, z in cells:
            tmp = 0
            for i, j, k in get_3d_neighbours(x, y, z):
                if (i, j, k) in cells:
                    tmp += 1
                check_area.add((i, j, k))
            if 2 <= tmp <= 3:
                new_cells.add((x, y, z))

        for x, y, z in check_area:
            tmp = 0
            for i, j, k in get_3d_neighbours(x, y, z):
                if (i, j, k) in cells:
                    tmp += 1
            if tmp == 3:
                new_cells.add((x, y, z))

        cells = new_cells

    return len(cells)

def solution2(f):

    cells = set()
    z, w = 0, 0

    for y, line in enumerate(f):
        for x, value in enumerate(line.strip()):
            if value == "#":
                cells.add((x, y, z, w))

    for _ in range(6):
        check_area = set()
        new_cells = set()

        for x, y, z, w in cells:
            tmp = 0
            for i, j, k, l in get_4d_neighbours(x, y, z, w):
                if (i, j, k, l) in cells:
                    tmp += 1
                check_area.add((i, j, k, l))
            if 2 <= tmp <= 3:
                new_cells.add((x, y, z, w))

        for x, y, z, w in check_area:
            tmp = 0
            for i, j, k, l in get_4d_neighbours(x, y, z, w):
                if (i, j, k, l) in cells:
                    tmp += 1
            if tmp == 3:
                new_cells.add((x, y, z, w))

        cells = new_cells

    return len(cells)

if __name__ == "__main__":
    with open("day17.txt") as f:
        print(solution1(f))
    with open("day17.txt") as f:
        print(solution2(f))
