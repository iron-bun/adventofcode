#!/usr/bin/env python3

test_data = ["R 6 (#70c710)",
"D 5 (#0dc571)",
"L 2 (#5713f0)",
"D 2 (#d2c081)",
"R 2 (#59c680)",
"D 2 (#411b91)",
"L 5 (#8ceee2)",
"U 2 (#caa173)",
"L 1 (#1b58a2)",
"U 2 (#caa171)",
"R 2 (#7807d2)",
"U 3 (#a77fa3)",
"L 2 (#015232)",
"U 2 (#7a21e3)"]


def calculate_area(data):
  circumference = 0
  coordinates = [(0,0)]
  x, y = 0, 0

  for line in data:
    line = line.strip()
    direction, distance, colour = line.split(" ")
    distance = int(distance)

    circumference += distance
    if direction == "R":
      x += distance
    elif direction == "D":
      y += distance
    elif direction == "L":
      x -= distance
    else:
      y -= distance

    coordinates.append((x, y))

  area = 0
  for idx in range(len(coordinates)):
    area += coordinates[idx][0] * (coordinates[idx-1][1] - coordinates[(idx+1)%len(coordinates)][1])
  area //= 2
  area = abs(area)
  area += circumference//2
  area += 1
  return area

with open("day18.txt") as f:
  data = f.readlines()
  print(calculate_area(data))

directions = {"0":"R", "1":"D", "2":"L", "3":"U"}
with open("day18.txt") as f:
  data = f.readlines()
  replacement_data = []

  for line in data:
    line = line.strip()
    direction, distance, colour = line.split(" ")
    colour = colour[2:-1]
    direction = directions[colour[-1]]
    distance = int(colour[:-1], 16)
    replacement_data.append(f"{direction} {distance} ###")

  print(calculate_area(replacement_data))

