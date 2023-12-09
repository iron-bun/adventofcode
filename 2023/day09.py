#!/usr/bin/env python3

test_data = ["0 3 6 9 12 15",
"1 3 6 10 15 21",
"10 13 16 21 30 45"]

def derive(data, forward=True):
  diffs = set(data)
  if len(diffs) == 1:
    return diffs.pop()

  tmp = [b-a for a, b in zip(data, data[1:])]
  tmp_d = derive(tmp, forward)
  if forward:
    return data[-1] + tmp_d
  else:
    return data[0] - tmp_d

ans = 0
with open("day09.txt") as data:
  for line in data:
    line = line.strip()
    line = list(map(int, line.split(" ")))
    tmp = derive(line)
    ans += tmp
print(ans)

ans = 0
with open("day09.txt") as data:
  for line in data:
    line = line.strip()
    line = list(map(int, line.split(" ")))
    tmp = derive(line, False)
    ans += tmp
print(ans)
