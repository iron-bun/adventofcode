#!/usr/bin/env python3

def find_sum(v, data):
    for i, j in enumerate(data):
        for k in data[i+1:]:
            if j+k == v:
                return True
    return False

def solution1(f):
    data = []
    while len(data) < 25:
        data.append(int(f.readline()))

    while True:
        tmp = int(f.readline())
        if not find_sum(tmp, data):
            return tmp
        data.pop(0)
        data.append(tmp)

def solution2(target, f):

    numbers = []
    while True:
        if sum(numbers) == target and len(numbers) > 1:
            return min(numbers) + max(numbers)
        elif sum(numbers) > target:
            numbers.pop(0)
        else:
            numbers.append(int(f.readline()))

if __name__ == "__main__":
    with open("day9.txt") as f:
        tmp = solution1(f)
        print(tmp)
    with open("day9.txt") as f:
        print(solution2(tmp, f))
