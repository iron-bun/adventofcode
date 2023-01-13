#!/usr/bin/env python3

def solution(f, target):
    init = list(map(int, f.readline().split(",")))

    history = {v:i+1 for i, v in enumerate(init[:-1])}

    idx = len(init)
    prev = init[-1]

    while idx < target:
        if prev not in history:
            history[prev] = idx
            new = 0
        else:
            new = idx - history[prev]
            history[prev] = idx
        idx += 1
        prev = new
    return prev

if __name__ == "__main__":
    with open("day15.txt") as f:
        print(solution(f, 2020))
    with open("day15.txt") as f:
        print(solution(f, 30000000))
