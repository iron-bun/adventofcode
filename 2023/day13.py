#!/usr/bin/env python3

test_data = ["#.##..##.",
"..#.##.#.",
"##......#",
"##......#",
"..#.##.#.",
"..##..##.",
"#.#.##.#.",
"",
"#...##..#",
"#....#..#",
"..##..###",
"#####.##.",
"#####.##.",
"..##..###",
"#....#..#"]

def count_reflections(mirror, desired_defects):
  ans = 0
  for candidate in range(1, len(mirror)):
   offset = 0
   defect_count = 0
   while candidate - offset - 1>= 0 and candidate + offset < len(mirror): 
      for a, b in zip(mirror[candidate - offset - 1], mirror[candidate + offset]):
        if a!=b:
          defect_count += 1
        if defect_count > desired_defects:
          offset = len(mirror)
          break
      offset += 1
   else:
     if defect_count == desired_defects:
       ans += 100*candidate

  for candidate in range(1, len(mirror[0])):
   offset = 0
   defect_count = 0
   while candidate - offset - 1>= 0 and candidate + offset < len(mirror[0]): 
      for a, b in zip(tuple(v[candidate - offset - 1] for v in mirror), tuple(v[candidate + offset] for v in mirror)):
        if a!=b:
          defect_count += 1
        if defect_count > desired_defects:
          offset = len(mirror)
          break
      offset += 1
   else:
     if defect_count == desired_defects:
       ans += candidate

  return ans

def parse_mirrors(data, desired_defects):

  mirror = []
  idx = 0
  ans = 0
  for line in data:
    line = line.strip()

    if line == "":
      ans += count_reflections(mirror, desired_defects)
      mirror = []
      hreflection_candidates = []
      idx = 0
      continue

    tmp = tuple(line)

    mirror.append(tmp)
    idx += 1

  ans += count_reflections(mirror, desired_defects)
  return ans

with open("day13.txt") as f:
  print(parse_mirrors(f, 0))

with open("day13.txt") as f:
  print(parse_mirrors(f, 1))
