#!/usr/bin/env python3

test_data = ["#.#.### 1,1,3",
".#...#....###. 1,1,3",
".#.###.#.###### 1,3,1,6",
"####.#...#... 4,1,1",
"#....######..#####. 1,6,5",
".###.##....# 3,2,1"]

unknown_test_data = ["???.### 1,1,3",
".??..??...?##. 1,1,3",
"?#?#?#?#?#?#?#? 1,3,1,6",
"????.#...#... 4,1,1",
"????.######..#####. 1,6,5",
"?###???????? 3,2,1"]

memo = {}
def fit_record(record, counts):
  if (record, counts) in memo:
    return memo[record, counts]

  if len(counts) > 0:
    pass
  elif "#" in record:
    return 0
  else:
    return 1

  if len(record) < sum(counts) + len(counts) - 1:
    return 0

  ans = 0
  count = counts[0]

  idx = 0
  while idx < len(record)+1-count:
    if "#" in record[:idx]:
      break

    if "." in record[idx:idx+count]:
      idx += 1
      continue

    if len(record) > idx+count and record[idx+count] == "#":
      idx += 1
      continue

    tmp = fit_record(record[idx+count+1:], counts[1:])
    memo[(record[idx+count+1:], counts[1:])] = tmp

    ans += tmp
    idx += 1

  return ans

total = 0
with open("day12.txt") as data:
  for line in data:
    line = line.strip()

    record, counts = line.split()
    counts = tuple(map(int, counts.split(",")))

    tmp_count = fit_record(record, counts)
    total += tmp_count
print(total)

total = 0
with open("day12.txt") as data:
  for line in data:
    line = line.strip()

    record, counts = line.split()
    counts = tuple(map(int, counts.split(",")))

    record = "?".join([record]*5)
    counts = counts*5

    tmp_count = fit_record(record, counts)
    total += tmp_count
print(total)


