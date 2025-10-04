#!/usr/bin/env python3

from intcode import Intcode

with open("day02.txt") as f:
    line = f.readline().strip().split(",")
    line = list(map(int, line))

    p = line.copy()
    p[1] = 12
    p[2] = 2
    p = Intcode(None, None, p).run()
    print(p[0])

    found = False
    for noun in range(99):
        for verb in range(99):

            p = line.copy()
            p[1] = noun
            p[2] = verb

            p = Intcode(None, None, p).run()

            if p[0] == 19690720:
                print(noun*100 + verb)
                found = True
                break
        if found:
            break
