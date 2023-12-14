#!/usr/bin/env python3

from copy import deepcopy

test_data = ["O....#....",
"O.OO#....#",
".....##...",
"OO.#O....O",
".O.....O#.",
"O.#..O.#.#",
"..O..#O..O",
".......O..",
"#....###..",
"#OO..#...."]

def roll_rocks(platform):
  positions = [0 for _ in platform[0]]
  new_platform = [['.' for _ in platform[0]] for _ in platform]

  for i, line in enumerate(platform):
    for j, char in enumerate(line):
      if char == "O":
        new_platform[positions[j]][j] = "O"
        positions[j] += 1
      if char == "#":
        new_platform[i][j] = "#"
        positions[j] = i + 1

  return new_platform

def rotate_platform(platform):
  new_platform = list(zip(*platform[::-1]))
  return new_platform

def score_platform(platform):
  ans = 0
  tmp = len(platform)

  for i, line in enumerate(platform):
    for j, char in enumerate(line):
      if char == "O":
        ans += tmp - i
  return ans

with open("day14.txt") as f:
  data = f.readlines()
  data = list(map(str.strip, data))
  data = [[c for c in line] for line in data]
  data = roll_rocks(data)
  print(score_platform(data))


with open("day14.txt") as f:
  data = f.readlines()
  data = list(map(str.strip, data))
  data = [[c for c in line] for line in data]
  line_length = len(data)

  idx = 1_000_000_000
  history = []

  while idx > 0:
    idx -= 1
    for _ in range(4):
      data = roll_rocks(data)
      data = rotate_platform(data)

    tmp = deepcopy(data)

    if tmp in history:
      idx = idx % (len(history) - history.index(tmp))
      data = history[history.index(tmp)+idx]
      break

    history.append(tmp)

  print(score_platform(data))

