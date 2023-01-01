#!/usr/bin/env python3


def solution1(f):
    data = map(int, f.readlines())
    data = sorted(data)

    ones = 1
    threes = 1
    for i, j in zip(data, data[1:]):
        if j-i == 1:
            ones += 1
        elif j-i == 3:
            threes += 1
            
    return ones * threes

def solution2(f):
    data = map(int, f.readlines())
    data = {v:0 for v in data}

    last_adapter = max(data.keys()) + 3

    data[0] = 1
    data[last_adapter] = 0

    for k in sorted(data.keys()):
        data[k] = data.get(k-3, 0) + data.get(k-2, 0) + data.get(k-1,0) + data[k]

    return data[last_adapter]    

if __name__ == "__main__":
    with open("day10.txt") as f:
        print(solution1(f))
    with open("day10.txt") as f:
        print(solution2(f))

