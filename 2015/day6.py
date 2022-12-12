#!/usr/bin/env python3

def part1():

    regions = {}
    puzzle_input = open("./data/day6.txt", "r")

    for line in puzzle_input:
        line = line.strip().split(" ")
        if line[0] == "toggle":
            x1, y1 = list(map(int, line[1].split(",")))
            x2, y2 = list(map(int, line[3].split(",")))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    regions[i, j] = not regions.get((i, j), False)

        elif line[1] == "on":
            x1, y1 = list(map(int, line[2].split(",")))
            x2, y2 = list(map(int, line[4].split(",")))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    regions[i, j] = True
        else:
            x1, y1 = list(map(int, line[2].split(",")))
            x2, y2 = list(map(int, line[4].split(",")))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    regions[i, j] = False
    return sum([1 for k, v in regions.items() if v])

def part2():

    regions = {}
    puzzle_input = open("./data/day6.txt", "r")

    for line in puzzle_input:
        line = line.strip().split(" ")
        if line[0] == "toggle":
            x1, y1 = list(map(int, line[1].split(",")))
            x2, y2 = list(map(int, line[3].split(",")))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    regions[i, j] = regions.get((i, j), 0) + 2

        elif line[1] == "on":
            x1, y1 = list(map(int, line[2].split(",")))
            x2, y2 = list(map(int, line[4].split(",")))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    regions[i, j] = regions.get((i, j), 0) + 1
        else:
            x1, y1 = list(map(int, line[2].split(",")))
            x2, y2 = list(map(int, line[4].split(",")))
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    regions[i, j] = max(0, regions.get((i, j), 0) - 1)

    return sum([v for k, v in regions.items()])

if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
