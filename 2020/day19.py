#!/usr/bin/env python3

from lark import Lark


def solution1(f):

    grammar = ""
    for line in f:
        if line == "\n":
            break
        line = line.strip().split(" ")
        line[0] = "a" + line[0]
        for idx in range(1, len(line)):
            if line[idx].isnumeric():
                line[idx] = "a" + line[idx]
        grammar += " ".join(line) + "\n"

    parser = Lark(grammar, start="a0")

    ans = 0
    for line in f:
        line = line.strip()
        try:
            parser.parse(line)
            ans += 1
        except Exception as e:
            pass

    return ans

def solution2(f):

    grammar = ""
    for line in f:
        if line == "\n":
            break
        if line[0:2] == "8:":
            line = "8: 42 | 42 8"
        if line[0:3] == "11:":
            line = "11: 42 31 | 42 11 31"

        line = line.strip().split(" ")
        line[0] = "a" + line[0]
        for idx in range(1, len(line)):
            if line[idx].isnumeric():
                line[idx] = "a" + line[idx]
        grammar += " ".join(line) + "\n"

    parser = Lark(grammar, start="a0")

    ans = 0
    for line in f:
        line = line.strip()
        try:
            parser.parse(line)
            ans += 1
        except Exception as e:
            pass

    return ans


if __name__ == "__main__":
    with open("day19.txt") as f:
        print(solution1(f))
    with open("day19.txt") as f:
        print(solution2(f))
