#!/usr/bin/env python3

with open("day02.txt") as f:
   data = f.readline().strip().split(",")

ranges = {}
for line in data:
    tmp = line.split("-")
    k, v = int(tmp[0]), int(tmp[1])

    ranges[k] = v

test_idx = 0
test_value = 0
ans = 0
for k, v in sorted(ranges.items(), key=lambda x: x[0]):
  while test_value < k:
    test_idx += 1
    test_value = int(f"{test_idx}"*2)

  while test_value <= v:
    ans += test_value
    test_idx += 1
    test_value = int(f"{test_idx}"*2)
print(ans)

ans = set()
for k, v in sorted(ranges.items(), key=lambda x: x[0]):
  for len_multiplier in range(2, len(f"{v}")+1):
    test_idx = 0
    test_value = 0

    while test_value < k:
      test_idx += 1
      test_value = int(f"{test_idx}"*len_multiplier)

    while test_value <= v:
      ans.add(test_value)
      test_idx += 1
      test_value = int(f"{test_idx}"*len_multiplier)
print(sum(ans))
