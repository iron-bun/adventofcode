#!/usr/bin/env python3

keys = []
locks = []

with open("day25.txt") as f:
    found = False
    lock = False
    pins = {}
    for line in f:
        line = line.strip()
        if line == "":

            if lock:
                locks.append([pins[k] for k in sorted(pins)])
            else:
                keys.append([pins[k] for k in sorted(pins)])
            found = False
            pins = {}
            continue
        
        if not found:
            if line[0] == "#":
                lock = True
            else:
                lock = False
            found = True
        for i, c in enumerate(line):
            if c == "#":
                pins[i] = pins.get(i, -1) + 1

    if lock:
        locks.append([pins[k] for k in sorted(pins)])
    else:
        keys.append([pins[k] for k in sorted(pins)])
        found = False
        pins = {}
        
ans = 0
for l in locks:
    for k in keys:
        for p1, p2 in zip(l, k):
            if p1+p2 > 5:
                break
        else:
            ans += 1

print(ans)


