#!/usr/bin/env python3

stopped_zero_count = 0
passed_zero_count = 0
dial_position = 50

with open("day01.txt") as f:
  for line in f:
    line = line.strip()
    direction, distance = line[0], int(line[1:])

    if direction == "L" and dial_position ==0:
        passed_zero_count -= 1

    while distance > 99:
        distance -= 100
        passed_zero_count += 1

    if direction == "L":
        distance *= -1

    dial_position += distance

    if dial_position < 0:
        passed_zero_count += 1
        dial_position += 100
    elif dial_position > 99:
        passed_zero_count += 1
        dial_position -= 100

    if dial_position == 0:
        stopped_zero_count += 1
        if direction == "L":
          passed_zero_count += 1

print(stopped_zero_count)
print(passed_zero_count)
