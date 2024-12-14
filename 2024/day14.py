#!/usr/bin/env python3

import re

boundx = 50
boundy = 51
quadrants = [0,0,0,0]

def advance_robot(x, y, vx, vy, width, height, seconds):
  return (x+vx*seconds)%width, (y+vy*seconds)%height

with open("day14.txt") as f:
  for line in f:
    x, y, vx, vy = list(map(int, re.findall("(-?\d+)", line)))
    x, y = advance_robot(x, y, vx, vy, 101, 103, 100)

    if x < boundx and y < boundy:
        quadrants[0] += 1
    elif x < boundx and y > boundy:
        quadrants[1] += 1
    elif x > boundx and y < boundy:
        quadrants[2] += 1
    elif x > boundx and y > boundy:
        quadrants[3] += 1

ans = 1
for q in quadrants:
    ans *= q
print(ans)

robots = []
with open("day14.txt") as f:
    for line in f:
        x, y, vx, vy = list(map(int, re.findall("(-?\d+)", line)))
        robots.append([x, y, vx, vy])

seconds = 43
tmp = []
for robot in robots:
    robot[0], robot[1] = advance_robot(*robot, 101, 103, seconds)
    tmp.append(robot)

robots = tmp
clockspeed = 103
complete = False

while True:
    locations = {}

    for robot in robots:
        locations[robot[0],robot[1]] = "#"

    line = ""
    for y in range(103):
        for x in range(101):
            line += locations.get((x,y), " ")
        if "##########" in line:
           complete = True
           ans = seconds

    if complete:
      break

    tmp = []
    seconds += clockspeed

    for robot in robots:
        robot[0], robot[1] = advance_robot(*robot, 101, 103, clockspeed)
        tmp.append(robot)
    robots = tmp

for y in range(103):
    for x in range(101):
        print(locations.get((x,y), " "), end="")
    print()
print(ans)

