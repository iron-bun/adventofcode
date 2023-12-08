#!/usr/bin/env python3

test_data = ["LLR",
"",
"AAA = (BBB, BBB)",
"BBB = (AAA, ZZZ)",
"ZZZ = (ZZZ, ZZZ)"]

def parse_file(data):
  instructions = ""
  desert_map = {}
  for line in data:
    line = line.strip()
    if line == "":
      continue
    if instructions == "":
      instructions = line
    else:
      n = (line[7:10], line[12:15])
      desert_map[line[0:3]]=n
  return instructions, desert_map

def count_moves(start, desert, part1=True):
  moves = 0
  idx = 0
  loc = start
  searching = True
  while searching:
    if instructions[idx] == "L":
      loc = desert[loc][0]
    else:
      loc = desert[loc][1]
    idx += 1
    if idx == len(instructions):
      idx = 0
    moves += 1
    if part1 and loc == "ZZZ":
      searching = False
    elif not part1 and loc[2] == "Z":
      searching = False
  return moves

def get_prime_factors(candidate):
  results = {}
  prime = 2
  while candidate > 1:
    while candidate % prime == 0:
      results[prime] = results.get(prime, 0) + 1
      candidate /= prime
    prime += 1
  return results

with open("day08.txt") as f:
  instructions, desert = parse_file(f)
print(count_moves("AAA", desert))

distances = []
for k in desert.keys():
  if k[2] == "A":
    distances.append(count_moves(k, desert, False))
factors = {}
for distance in distances:
  f = get_prime_factors(distance)
  for k, v in f.items():
    tmp = factors.get(k, 0)
    if v > tmp:
      factors[k] = v
ans = 1
for k,v in factors.items():
  ans *= k**v
print(ans)    
