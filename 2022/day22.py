#!/usr/bin/env python3
import re

def get_directions(direction):
    pos = 0
    expression = re.compile("\d+")
    while True:
        ans = expression.search(direction, pos)
        if ans == None:
            break
        yield int(ans.group(0))
        pos = ans.span()[1]
        if pos < len(direction):
            yield direction[pos]
        pos += 1
        
def parse(f):
    data = []
    for line in f:
        if line == "\n":
            break

        data.append(line.strip("\n"))
    start = (data[0].index("."), 0)
    directions = f.readline().strip()

    return data, start, directions

turns = {"e":{"L":'n', "R":'s', "s":0}, "n":{"L":"w", "R":"e", "s":3}, "s":{"L":"e", "R":"w", "s":2}, "w":{"L":'s', "R":"n", "s":2}}

def solution1(data):
    data, start, directions = data
    facing = "e"

    for action in get_directions(directions):
        if type(action) == str:
            facing = turns[facing][action]
        else:
            x, y = start
            for _ in range(action):
                if facing == "e":
                    x += 1
                    if x >= len(data[y]):
                        x = re.search("#|\.", data[y]).span()[0]
                elif facing == "w":
                    x -= 1
                    if x < 0 or data[y][x] == " ":
                        x = len(data[y]) - 1
                        while data[y][x] not in ("#","."):
                            x -= 1
                elif facing == "s":
                    y += 1
                    if y >= len(data) or x >= len(data[y]) or data[y][x] == " ":
                        y = 0
                        while data[y][x] not in ('#','.'):
                            y += 1
                elif facing == "n":
                    y -= 1
                    if y < 0 or data[y][x] not in ('#','.'):
                        y = len(data)-1
                        while x >= len(data[y]) or data[y][x] not in ('#','.'):
                            y -= 1
                else:
                    print("unknown direction", start)

                if data[y][x] != ".":
                    break
                start = (x, y)
    x, y = start
    x += 1
    y += 1
    return 1000*y + 4*x + turns[facing]["s"]

def solution2(data):
    data, start, directions = data
    start = (start[0], start[1], "e")

    for action in get_directions(directions):
        x, y, f = start
        if type(action) == str:
            f = turns[f][action]
            start = (x, y, f)
        else:
            for _ in range(action):
                if f == "e":
                    x += 1
                    if x >= len(data[y]):
                        if y < 50:
                            y = 149 - y
                            x = 99
                            f = "w"
                        elif y < 100:
                            x = y + 50
                            y = 49
                            f = "n"
                        elif y < 150:
                            y = 149 - y
                            x = 149
                            f = "w"
                        else:
                            x = y - 100
                            y = 149
                            f = "n"
                elif f == "s":
                    y += 1
                    if y >= len(data) or x >= len(data[y]):
                        if y == 50:
                            y = x - 50
                            x = 99
                            f = "w"
                        elif y == 150:
                            y = 100 + x
                            x = 49
                            f = "w"
                        elif y == 200:
                            x = x + 100
                            y = 0
                            f = "s"
                elif f == "w":
                    x -= 1
                    if x < 0 or data[y][x] == " ":
                        if y < 50:
                            x = 0
                            y = 149 - y
                            f = "e"
                        elif y < 100:
                            x = y - 50
                            y = 100
                            f = "s"
                        elif y < 150:
                            y = 149 - y
                            x = 50
                            f = "e"
                        else:
                            x = y - 100
                            y = 0
                            f = "s"
                elif f == "n":
                    y -= 1
                    if y < 0 or data[y][x] == " ":
                        if y == 99:
                            y = 50+x
                            x = 50
                            f = "e"
                        elif x < 100:
                            y = 100 + x
                            x = 0
                            f = "e"
                        else:
                            x = x - 100
                            y = 199
                            f = "n"
                else:
                    print(f"unknown direction {f}")
                    exit()

                if data[y][x] != ".":
                    break
                start = (x, y, f)

    x, y, f = start
    x += 1
    y += 1
    return 1000*y + 4*x + turns[f]["s"]


if __name__ == "__main__":
    with open("day22.txt") as f:
        data = parse(f)
    print(solution1(data))
    print(solution2(data))

#121382 too high
#14292 too low
