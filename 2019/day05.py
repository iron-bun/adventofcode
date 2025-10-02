#!/usr/bin/env python3

from intcode import run

with open("day05.txt") as f:
    line = f.readline().strip().split(",")
    line = list(map(int, line))

    p = line.copy()
    p = run(p, 1)

    p = line.copy()
    p = run(p, 5)
