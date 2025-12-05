#!/usr/bin/env python3

def merge_ranges(new_range, old_ranges):
    fresh_ranges = []
    for old_range in old_ranges:
      if new_range == None:
        fresh_ranges.append(old_range)

      #an existing range is fully contained in the new range. Discard old
      elif old_range[0] >= new_range[0] and old_range[1] <= new_range[1]:
        pass

      #an existing range completely encloses the new range. Discard new
      elif new_range[0] >= old_range[0] and new_range[1] <= old_range[1]:
        new_range = None
        fresh_ranges.append(old_range)

      #new range overlaps the old range to the high end
      elif old_range[0] <= new_range[0] <= old_range[1]+1 and new_range[1] > old_range[1]+1:
        fresh_ranges.append((old_range[0], new_range[1]))
        new_range = None

      #new range overlaps the old range to the low end
      elif new_range[0] < old_range[0]-1 and old_range[0]-1 <= new_range[1] <= old_range[1]:
        fresh_ranges.append((new_range[0], old_range[1]))
        new_range = None

      #old range and new range are completely disjoint
      else:
         fresh_ranges.append(old_range)
    if new_range != None:
      fresh_ranges.append(new_range)

    return fresh_ranges

fresh_ranges = []
with open("day05.txt") as f:
  for line in f:
    line = line.strip()
    if line == "":
      break

    new_range = tuple(map(int, line.split("-")))
    old_ranges = fresh_ranges
    fresh_ranges = merge_ranges(new_range, old_ranges)

  old_ranges = None
  while old_ranges == None or len(old_ranges) != len(fresh_ranges):
    old_ranges = fresh_ranges
    fresh_ranges = []
    for new_range in old_ranges:
      fresh_ranges = merge_ranges(new_range, fresh_ranges)

  ans = 0
  for line in f:
    for fresh_range in fresh_ranges:
      if fresh_range[0] <= int(line) <= fresh_range[1]:
        ans += 1
        break
print(ans)

ans = 0
for fresh_range in fresh_ranges:
  ans += fresh_range[1] - fresh_range[0] + 1
print(ans)
