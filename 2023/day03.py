#!/usr/bin/env python3

data = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]

def parse_data(data):
  result = {}
  width, height = 0, 0
  for idx, line in enumerate(data):
    line = line.strip()
    for idx2, char in enumerate(line):
        result[(idx2, idx)] = char
        width = idx2
    height = idx
  return result, width+1, height+1

def read_data(x, y, data):
  if (x, y) not in data:
    return "."
  else:
    return data[(x, y)]

gears = {}

def generate_parts(data, width, height):
  number = ""
  part = False
  gears_found = []

  for j in range(height):
    for i in range(width):
      tmp = read_data(i, j, data)
      if tmp in "1234567890":
        number += tmp
        for k in range(-1, 2):
          for l in range(-1, 2):
            if (k, l) == (0,0):
              continue
            tmp2 = read_data(i+k, j+l, data)
            if tmp2 == "*" and (i+k, j+l) not in gears_found:
              gears_found.append((i+k, j+l))
            if tmp2 not in "1234567890.":
              part = True
      elif part:
        yield int(number)
        for gear in gears_found:
          gears[gear] = gears.get(gear, []) + [int(number)]
        gears_found = []
        number = ""
        part = False
      else:
        number = ""

with open("day03.txt") as data:
  schematic, width, height = parse_data(data)
  total = 0
  for i in generate_parts(schematic, width, height):
    total += i
  print(total)

total = 0
for loc, g in gears.items():
    if len(g) == 2:
        total += g[0] * g[1]
print(total)
