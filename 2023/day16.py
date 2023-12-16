#!/usr/bin/env python3

test_data = [".|...\\....",
"|.-.\\.....",
".....|-...",
"........|.",
"..........",
".........\\",
"..../.\\\\..",
".-.-/..|..",
".|....-|.\\",
"..//.|...."]

def follow_beam(x, y, direction, data):
  if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
    return [], []

  squares_illuminated = [(x, y)]
  next_mirror = []
  while True:
    if data[y][x] == ".":
      if direction == "N": y -= 1
      if direction == "S": y += 1
      if direction == "E": x += 1
      if direction == "W": x -= 1
      if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        break
      squares_illuminated.append((x, y))


    if data[y][x] != ".":
      next_mirror = [(x, y, direction)]
      break
  return squares_illuminated, next_mirror
 
mirrors = {}
def parse_mirrors(data):
  for i, line in enumerate(data):
    for j, char in enumerate(line):
      if char == ".":
        continue
      for d in "NSEW":
        #print(j, i, d, char)
        if char == "|":
          if d in "EW":
            tmp1 = follow_beam(j, i-1, "N", data)
            tmp2 = follow_beam(j, i+1, "S", data)
            tmp = tmp1[0] + tmp2[0], tmp1[1] + tmp2[1]
          if d == "N":
            tmp = follow_beam(j, i-1, "N", data)
          if d == "S":
            tmp = follow_beam(j, i+1, "S", data)
        if char == "-":
          if d in "NS":
            tmp1 = follow_beam(j+1, i, "E", data)
            tmp2 = follow_beam(j-1, i, "W", data)
            tmp = tmp1[0] + tmp2[0], tmp1[1] + tmp2[1]
          if d == "E":
            tmp = follow_beam(j+1, i, "E", data)
          if d == "W":
            tmp = follow_beam(j-1, i, "W", data)
        if char == "/":
          if d == "N":
            tmp = follow_beam(j+1, i, "E", data)
          if d == "S":
            tmp = follow_beam(j-1, i, "W", data)
          if d == "E":
            tmp = follow_beam(j, i-1, "N", data)
          if d == "W":
            tmp = follow_beam(j, i+1, "S", data)
        if char == "\\":
          if d == "N":
            tmp = follow_beam(j-1, i, "W", data)
          if d == "S":
            tmp = follow_beam(j+1, i, "E", data)
          if d == "E":
            tmp = follow_beam(j, i+1, "S", data)
          if d == "W":
            tmp = follow_beam(j, i-1, "N", data)
        #print(j, i, char, d, tmp)
        mirrors[j, i, d] = tmp

def count_squares(x, y, d, data):
  squares = []

  while x >= 0 and x < len(data[0]) and y >= 0 and y < len(data) and data[y][x] == ".":
    squares.append((x, y))
    if d == "E":
      x += 1
    if d == "W":
      x -= 1
    if d == "N":
      y -= 1
    if d == "S":
      y += 1

  squares.append((x, y))
  if x < 0 or x == len(data[0]) or y < 0 or y == len(data):
    return len(set(squares))

  next_squares = [(x, y, d)]

  illuminated_mirrors = []

  while len(next_squares) > 0:
    x, y, d = next_squares.pop()
    if (x, y, d) in illuminated_mirrors:
      continue
    illuminated_mirrors.append((x, y, d))
    tmp = mirrors[x, y, d]
    squares += tmp[0]
    if tmp[1] != None:
      next_squares += tmp[1]
  return len(set(squares))

with open("day16.txt") as f:
  data = list(map(str.strip, f.readlines()))
  #data = test_data
parse_mirrors(data)

print(count_squares(0, 0, "E", data))

ans = 0
for i in range(len(data[0])):
  tmp = count_squares(i, 0, "S", data)
  if tmp > ans:
    ans = tmp
for i in range(len(data[0])):
  tmp = count_squares(i, len(data[0])-1, "N", data)
  if tmp > ans:
    ans = tmp
for i in range(len(data)):
  tmp = count_squares(0, i, "E", data)
  if tmp > ans:
    ans = tmp
for i in range(len(data)):
  tmp = count_squares(len(data[0])-1, i, "W", data)
  if tmp > ans:
    ans = tmp
print(ans)
