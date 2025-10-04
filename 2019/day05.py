#!/usr/bin/env python3

from intcode import Intcode
from queue import Queue

with open("day05.txt") as f:
    line = f.readline().strip().split(",")
    line = list(map(int, line))

    q1 = Queue()
    q2 = Queue()

    q1.put(1)
    p = line.copy()
    p = Intcode(q1, q2, p).run()
    while not q2.empty():
        print(q2.get())

    q1.put(5)
    p = line.copy()
    p = Intcode(q1, q2, p).run()
    print(q2.get())
