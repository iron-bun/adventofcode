#!/usr/bin/env python3

puzzle_input = "(())"
puzzle_input = open("./data/day1.txt", "r").readline()

def part1():
    ans = 0
    for c in puzzle_input.strip():
        if c =="(":
            ans += 1
        else:
            ans -= 1
    print("part 1", ans)

def part2():
    floor = 0
    ans = 0
    for c in puzzle_input.strip():
        if c =="(":
            floor += 1
        else:
            floor -= 1
        ans += 1
        if floor == -1:
            print("part 2", ans)
            break

if __name__ == '__main__':
    part1()
    part2()
