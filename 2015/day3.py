#!/usr/bin/env python3

def part1():

    deliveries = {(0,0)}
    x, y = 0, 0

    puzzle_input = open("./data/day3.txt", "r").readline().strip()

    for move in puzzle_input:
        if move == "^":
            x += 1
        elif move == "v":
            x -= 1
        elif move == ">":
            y += 1
        elif move == "<":
            y -= 1
        deliveries.add((x, y))
    return len(deliveries)

def part2():

        deliveries = {(0,0)}
        locations = [0, 0, 0, 0]
        offset = 0

        puzzle_input = open("./data/day3.txt", "r").readline().strip()

        for move in puzzle_input:
            if move == "^":
                locations[offset] += 1
            elif move == "v":
                locations[offset] -= 1
            elif move == ">":
                locations[offset+1] += 1
            elif move == "<":
                locations[offset+1] -= 1
                
            deliveries.add((locations[offset], locations[offset+1]))
            offset += 2
            offset %= 4

        return len(deliveries)


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
