#!/usr/bin/env python3

from queue import PriorityQueue

def dijkstra(start, generator, test_end):

  queue = PriorityQueue()
  resolved = set()

  queue.put((0, start))

  while queue.qsize() > 0:

    cost, node = queue.get()

    while queue.qsize() > 0 and node in resolved:
      cost, node = queue.get()

    for c, n in generator(node):
      queue.put((c+cost, n))

    if test_end(node):
      return cost

    resolved.add(node)

