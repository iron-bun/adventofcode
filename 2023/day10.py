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

def search(start, data):
  x, y = start
  count = 0

  for direction in directions.keys():
    path = [start]

    while True:
      offset, options = directions[direction]
      try:
        next_square = data[y+offset[1]][x+offset[0]]
      except:
        next_square = "."

      if next_square == "S":
        return count, path

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

circumference, path = search(find_start(data), data)
ans = int((circumference+1)/2)
print(ans)

#shoelace formula for the area of a polygon from its vertices
area = 0.5*sum([path[n][0]*(path[(n+1)%len(path)][1]-path[n-1][1]) for n in range(len(path))])
area = abs(area)

#Correct for the circumference taking up space
area -= ans
area += 1
print(int(area))
