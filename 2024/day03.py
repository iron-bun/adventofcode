#!/usr/bin/env python3

testdata = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

import re

with open("day03.txt") as f:
  data = f.readlines()

enabled = True
ans_part_1 = 0
ans_part_2 = 0
for line in data:
  for m in re.findall("(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", line):
    if m[0] == "don't()":
      enabled = False
      continue
    if m[0] == "do()":
      enabled = True
      continue
    if enabled:
      ans_part_2 += int(m[1]) * int(m[2])
    ans_part_1 += int(m[1]) * int(m[2])
print(ans_part_1)
print(ans_part_2)

