#!/usr/bin/env python3

def part1():

    puzzle_input = open("./data/day2.txt", "r")

    ans = 0
    for line in puzzle_input:
        line = line.strip().split("x")
        line = list(map(int, line))
        x, y, z = sorted(line)

        ans += x * y
        ans += 2 * x * y
        ans += 2 * y * z
        ans += 2 * x * z
    return ans

def part2():
    puzzle_input = open("./data/day2.txt", "r")

    ans = 0
    for line in puzzle_input:
        line = line.strip().split("x")
        line = list(map(int, line))
        x, y, z = sorted(line)

        ans += 2 * x + 2 * y
        ans += x * y * z
    return ans

if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
