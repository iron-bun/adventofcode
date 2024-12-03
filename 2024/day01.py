#!/usr/bin/env python3

with open("./day01.txt") as f:
  first, second = [], []
  for line in f:
    line = line.strip().split()
    first.append(int(line[0]))
    second.append(int(line[1]))

first = sorted(first)
second = sorted(second)

ans = 0
for a, b in zip(first, second):
  ans += abs(a-b)

print(ans)

second_count = {}

for b in second:
  second_count[b] = second_count.get(b, 0) + 1

ans = 0
for a in first:
  ans += a * second_count.get(a, 0)
print(ans)
