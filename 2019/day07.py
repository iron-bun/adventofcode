#!/usr/bin/env python3

from intcode import Intcode
from itertools import permutations
from queue import Queue
import threading

def amplify(p):

    queues = [Queue() for v in range(5)]

    computers = [Intcode(a, b, orig.copy()) for a, b in zip(queues, queues[1:])]
    computers.append(Intcode(queues[-1], queues[0], orig.copy()))

    threads = [threading.Thread(target=a.run) for a in computers]

    for t in threads:
        t.start()

    for q, v in zip(queues, p):
        q.put(v)

    queues[0].put(0)

    for t in threads:
        t.join()

    return queues[0].get()

with open("day07.txt") as f:
    orig = list(map(int, f.readline().split(",")))

ans = 0
for p in permutations([0,1,2,3,4]):
    tmp = amplify(p)
    if tmp > ans:
        ans = tmp
print(ans)

ans = 0
for p in permutations([5,6,7,8,9]):
    tmp = amplify(p)
    if tmp > ans:
        ans = tmp
print(ans)
