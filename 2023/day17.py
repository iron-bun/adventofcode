#!/usr/bin/env python3

from queue import PriorityQueue

test_data = ["2413432311323",
"3215453535623",
"3255245654254",
"3446585845452",
"4546657867536",
"1438598798454",
"4457876987766",
"3637877979653",
"4654967986887",
"4564679986453",
"1224686865563",
"2546548887735",
"4322674655533"]

def get_cost(x, y, data):
  return int(data[y][x])

def find_min_cost_route(start, end, data, min_step=1, max_step=3):

  queue = PriorityQueue()
  resolved = set()

  queue_item = (0, ((0,0), "."))
  queue.put(queue_item)

  while queue.qsize() > 0:

    cost, location = queue.get()
    location, steps = location
    x, y = location
    prev_step = steps[-1]

    while queue.qsize() > 0 and (x, y, prev_step) in resolved:
      cost, location = queue.get()
      location, steps = location
      prev_step = steps[-1]
      x, y = location

    if (x, y) == end:
      return cost

    if prev_step != ">":
      sum_cost = 0
      for i in range(1, max_step+1):
        if x-i < 0:
          break
        sum_cost += get_cost(x-i, y, data)
        if i >= min_step:
          next_cost = cost + sum_cost
          queue_item = (next_cost, ((x-i,y), ">"))
          queue.put(queue_item)

      sum_cost = 0
      for i in range(1, max_step+1):
        if x+i >= len(data[0]):
          break
        sum_cost += get_cost(x+i, y, data)
        if i >= min_step:
          next_cost = cost + sum_cost
          queue_item = (next_cost, ((x+i, y), ">"))
          queue.put(queue_item)

    if prev_step != "V":
      sum_cost = 0
      for i in range(1, max_step+1):
        if y-i < 0:
          break
        sum_cost += get_cost(x, y-i, data)
        if i >= min_step:
          next_cost = cost + sum_cost
          queue_item = (next_cost, ((x, y-i), "V"))
          queue.put(queue_item)

      sum_cost = 0
      for i in range(1, max_step+1):
        if y+i >= len(data):
          break
        sum_cost += get_cost(x, y+i, data)
        if i >= min_step:
          next_cost = cost + sum_cost
          queue_item = (next_cost, ((x, y+i), "V"))
          queue.put(queue_item)

    resolved.add((x, y, prev_step))


with open("day17.txt") as f:
  data = f.readlines()
  data = list(map(str.strip, data))

cost = find_min_cost_route((0,0), (len(data[0])-1, len(data)-1), data)
print(cost)

cost = find_min_cost_route((0,0), (len(data[0])-1, len(data)-1), data, 4, 10)
print(cost)

