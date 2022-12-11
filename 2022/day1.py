#!/usr/bin/env python3

ans = []

with open("day1.txt") as f:
   tmp = 0
   for line in f:
      line = line.strip()
      if line == "":
          ans.append(tmp)
          tmp = 0
      else:
          tmp += int(line)

ans = sorted(ans)
print(max(ans))
print(sum(ans[-4:-1]))
