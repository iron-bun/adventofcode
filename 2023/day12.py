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

def debug_print(*args):
  return
  print(*args)

def fit_record(record, counts):
  debug_print("//", record, counts)

  if len(counts) == 0:
    return

  min_length = sum(counts) + len(counts) - 1
  if min_length > len(record):
    #print("candidates don't fit in remaining space")
    return

  if record[0] == ".":
    for tmp in fit_record(record[1:], counts):
      yield "." + tmp
    return

  if min_length == len(record):
    test_record = ".".join("#"*v for v in counts)
    for i, j in zip(record, test_record):
      if i == "." and j == "#" or i == "#" and j == ".":
        break
    else:
      debug_print("Solution from only fit")
      yield ".".join("#"*v for v in counts)
    #print("only solution doesn't fit")
    return 

  ans = 0
  for idx in range(len(record)):
    if idx+counts[0] > len(record):
      break
    if "#" in record[:idx]:
      break
    if "." in record[idx:idx+counts[0]]:
      #print(f"Can't fit {counts[0]} into index {idx} ({record[idx:idx+counts[0]]} {counts[1:]})")
      continue
    if idx+counts[0] < len(record) and record[idx+counts[0]] == "#":
      #print(f"Can't fit {counts[0]} into index {idx} because trailing #")
      continue
    #print(f"{counts[0]} fits at index {idx} of {record}")
    if len(counts) > 1:
      for tmp in fit_record(record[idx+counts[0]+1:], counts[1:]):
        yield "."*idx + "#"*counts[0] + "." + tmp
    elif len(counts) == 1 and "#" in record[idx+counts[0]:]:
      pass
      #print("unallocated #")
    elif len(counts) == 1:
      yield "."*idx + "#"*counts[0] + "."*(len(record)-idx-counts[0])

total = 0
with open("day12.txt") as data:
  for line in data:
    line = line.strip()

    record, counts = line.split()
    counts = list(map(int, counts.split(",")))

    tmp_count = 0
    print(record, counts)
    for tmp in fit_record(record, counts):
      print(tmp)
      tmp_count += 1
    print("result count", tmp_count)
    total += tmp_count
print(total)


