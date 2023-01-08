#!/usr/bin/env python3


def manhatten_distance(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def solution1(f):
    x, y =  0, 0
    angle = 0
    directions = {0:"E", 90: "S", 180: "W", 270: "N"}

    for line in f:
        action, distance = line[0], int(line[1:])
        if action == "F":
            action = directions[angle]

        if action == "N":
            x += distance
        elif action == "E":
            y += distance
        elif action == "W":
            y -= distance
        elif action == "S":
            x -= distance
        elif action == "R":
            angle += distance
            angle %= 360
        elif action == "L":
            angle -= distance
            angle %= 360 

    return manhatten_distance((0,0), (x, y))

def solution2(f):
    x, y = 0, 0
    bx, by = 10, 1

    for line in f:
        action, distance = line[0], int(line[1:])

        if action == "N":
            by += distance
        elif action == "E":
            bx += distance
        elif action == "W":
            bx -= distance
        elif action == "S":
            by -= distance
        elif action == "R":
            for _ in range(int(distance/90)):
                bx, by = by, -bx
        elif action == "L":
            for _ in range(int(distance/90)):
                bx, by = -by, bx
        elif action == "F":
            for _ in range(distance):
                x, y = x + bx, y+by

    return manhatten_distance((0,0), (x,y))


if __name__ == "__main__":
    with open("day12.txt") as f:
        print(solution1(f))
    with open("day12.txt") as f:
        print(solution2(f))
