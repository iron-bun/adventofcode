#!/usr/bin/env python3

from intcode import Intcode
from queue import Queue

with open("day09.txt") as f:
    data = list(map(int, f.read().strip().split(",")))

q1 = Queue()
q2 = Queue()
ic = Intcode(q1, q2, data)

q1.put(1)
ic.run()
while not q2.empty():
    print(q2.get())

q1.put(2)
ic = Intcode(q1, q2, data)
ic.run()
while not q2.empty():
    print(q2.get())
