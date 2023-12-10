#!/usr/bin/env python3

test_data = ["7-F7-",
".FJ|7",
"SJLL7",
"|F--J",
"LJ.LJ"]

med_test_data = ["..........",
".S------7.",
".|F----7|.",
".||....||.",
".||....||.",
".|L-7F-J|.",
".|..||..|.",
".L--JL--J.",
".........."]

large_test_data = [".F----7F7F7F7F-7....",
".|F--7||||||||FJ....",
".||.FJ||||||||L7....",
"FJL7L7LJLJ||LJ.L-7..",
"L--J.L7...LJS7F-7L7.",
"....F-J..F7FJ|L7L7L7",
"....L7.F7||L7|.L7L7|",
".....|FJLJ|FJ|F7|.LJ",
"....FJL-7.||.||||...",
"....L---J.LJ.LJLJ..."]

def find_start(data):
  for i,line in enumerate(data):
    for j, char in enumerate(line):
      if char == "S":
        return j, i

directions={"N":((0,-1), {"7":"W", "|":"N", "F":"E"}),
            "E":((1, 0), {"7":"S", "-":"E", "J":"N"}),
            "W":((-1, 0),{"L":"N", "-":"W", "F":"S"}),
            "S":((0,1),  {"|":"S", "J":"W", "L":"E"})}

s_types = {"N":{"N":"|", "E":"J", "W":"L"},
           "E":{"N":"F", "E":"-", "S":"L"},
           "W":{"N":"7", "S":"J", "W":"-"},
           "S":{"S":"|", "E":"7", "W":"F"}}

def search(start, data):
  x, y = start
  count = 0

  for direction in directions.keys():
    path = [start]
    first_direction = direction

    while True:
      offset, options = directions[direction]
      try:
        next_square = data[y+offset[1]][x+offset[0]]
      except:
        next_square = "."

      if next_square == "S":
        return count, path, s_types[first_direction][direction]

      elif next_square in options.keys():
        x, y = x+offset[0], y+offset[1]
        path.append((x, y))
        direction = options[next_square]
        count += 1

      else:
        break

with open("day10.txt") as file:
  data = file.readlines()
  data = [list(l) for l in data]

count, path, s_type = search(find_start(data), data)
print(int((count+1)/2))

count = 0
path_marks = {"S":"S","|":"│", "L":"└", "7":"┐", "F":"┌", "J":"┘", "-":"─"}
for i, line in enumerate(data):
  inside=False
  last_cross = ""
  for j, char in enumerate(line):
    if (j, i) in path:
      data[i][j] = path_marks[char]

      if char == "S":
        char = s_type

      if char == "|":
        inside = not inside
        last_cross = ""

      elif last_cross == "" and char in "FL":
        inside = not inside
        last_cross = char
      elif last_cross == "F" and char == "J":
        last_cross = ""

      elif last_cross == "F" and char in "7":
        inside = not inside
        last_cross = ""

      elif last_cross == "L" and char == "7":
        last_cross = ""

      elif last_cross == "L" and char == "J":
        inside = not inside
        last_cross = ""

    elif inside:
      count += 1
      data[i][j] = "*"
    elif char!=".":
      data[i][j] = "X"

for line in data:
  print("".join(line).strip("\n"))
print(count)
