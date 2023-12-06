#!/usr/bin/env python3

# dist = held*(race-held)
#    0 = -held**2 + race*held - dist

from math import ceil, floor

def quadratic_formula(a, b, c):
  part1 = -1*b
  part2 = (b**2 - 4* a*c)**0.5
  part3 = 2*a

  return (part1 + part2)/part3, (part1 - part2)/part3

lines = ["Time:      7  15   30",
"Distance:  9  40  200"]

with open("day06.txt") as f:
  lines = f.readlines()

lines = [l.split() for l in lines]
lines = [l[1:] for l in lines]
lines = [list(map(int, l)) for l in lines]
total = 1

for race in zip(lines[0], lines[1]):
  a1, a2 = quadratic_formula(-1, race[0], -1*(race[1]+1))
  a1 -= 1
  a1, a2 = ceil(a1), floor(a2)
  total *= a2-a1
print(total)

total_time = int("".join(map(str, lines[0])))
total_dist = int("".join(map(str, lines[1])))

a1, a2 = quadratic_formula(-1, total_time, -1*(total_dist+1))
a1 -= 1
a1, a2 = ceil(a1), floor(a2)
total = a2-a1
print(total)
