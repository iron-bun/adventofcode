#!/usr/bin/env python3

from libs.dijkstra import dijkstra

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

def get_map_maker(min_step, max_step):
  min_step = min_step
  max_step = max_step

  def get_neighbours(tile):
    x, y, prev_step = tile

    if prev_step != ">":
      sum_cost = 0
      for i in range(1, max_step+1):
        if x-i < 0:
          break
        sum_cost += get_cost(x-i, y, data)
        if i >= min_step:
          yield (sum_cost, (x-i,y, ">"))

      sum_cost = 0
      for i in range(1, max_step+1):
        if x+i >= len(data[0]):
          break
        sum_cost += get_cost(x+i, y, data)
        if i >= min_step:
          yield (sum_cost, (x+i, y, ">"))

    if prev_step != "V":
      sum_cost = 0
      for i in range(1, max_step+1):
        if y-i < 0:
          break
        sum_cost += get_cost(x, y-i, data)
        if i >= min_step:
          yield (sum_cost, (x, y-i, "V"))

      sum_cost = 0
      for i in range(1, max_step+1):
        if y+i >= len(data):
          break
        sum_cost += get_cost(x, y+i, data)
        if i >= min_step:
          yield (sum_cost, (x, y+i, "V"))

  def end_found(node):
    return node[:2] == (len(data[0])-1, len(data)-1)

  return get_neighbours, end_found

with open("day17.txt") as f:
  data = f.readlines()
  data = list(map(str.strip, data))

map_maker, end_found = get_map_maker(1, 3)
cost = dijkstra((0,0,"."), map_maker, end_found)
print(cost)


map_maker, end_found = get_map_maker(4, 10)
cost = dijkstra((0,0,"."), map_maker, end_found)
print(cost)
