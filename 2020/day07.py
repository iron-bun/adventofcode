#!/usr/bin/env python3

def parse(line):
    if "contain no other bags" in line:
        return None, None
    line = line.strip().split(" ")
    bag = " ".join(line[:2])

    contains = []
    for i in range(4, len(line), 4):
        contains.append((" ".join(line[i+1:i+3]), int(line[i])))
    return bag, contains

def dfs(start, tree, result, multiplier):
    if start in tree:
        for item in tree[start]:
            item = item
            result.append((item[0], item[1]*multiplier))
            dfs(item[0], tree, result, item[1]*multiplier)
    return result

def solution1(f):
    contains = {}

    for line in f:
        line = parse(line)
        if line[0] == None:
            continue
        for bag in line[1]:
            bag = bag[0]
            if bag not in contains:
                contains[bag] = []
            contains[bag].append((line[0],0))

    return len(set(dfs("shiny gold", contains, list(), 0)))

def solution2(f):
    contains = {}
    ans = 0
    for line in f:
        if "contain no other bags" in line:
            continue
        bag, has = parse(line)
        if bag not in contains:
            contains[bag] = []
        for item in has:
            contains[bag].append(item)

    ans = dfs("shiny gold", contains, list(), 1)
    ans = sum([int(v[1]) for v in ans])
    return ans
    
if __name__ == "__main__":
    with open("day7.txt") as f:
        print(solution1(f))
    with open("day7.txt") as f:
        print(solution2(f))
