#!/usr/bin/env python3

with open("day01.txt") as f:
    ans_1 = 0
    ans_2 = 0

    for line in f:
        line = int(line)
        tmp = line//3 - 2
        ans_1 += tmp
        while tmp > 0:
            ans_2 += tmp
            tmp = tmp//3 - 2
    print(ans_1)
    print(ans_2)
