#!/usr/bin/env python3

test_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.split("\n")

with open("day06.txt") as data:
  sums = []
  for line_count, line in enumerate(data):
    line = tuple(v for v in line.split(" ") if v != "")
    sums.append(line)

ans = 0
for idx in range(len(sums[0])):
  if sums[line_count][idx] == "*":
    tmp = 1
    for idx2 in range(line_count):
       tmp *= int(sums[idx2][idx])
  else:
    tmp = 0
    for idx2 in range(line_count):
       tmp += int(sums[idx2][idx])
  ans += tmp
print(ans)

with open("day06.txt") as data:
  sums = data.readlines()
  #sums = test_data

ans = 0
numbers = []
for idx in range(len(sums[0])-1):
  symbol_found = False
  tmp = ""
  for idx2 in range(len(sums)):
    char = sums[idx2][idx]
    if char == "*":
      operator = "*"
      accumulator = 1
      symbol_found = True
    elif char == "+":
      operator = "+"
      accumulator = 0
      symbol_found = True
    elif char == " ":
      pass
    else:
      tmp += char
      symbol_found = True
  if not symbol_found:
    ans += accumulator
  elif operator == "*":
    accumulator *= int(tmp)
  else:
    accumulator += int(tmp)
ans += accumulator
print(ans)
