#!/usr/bin/env python3

with open("day11.txt") as f:
  data = list(map(int,f.readline().split()))

def evolve(stone):
  if stone == 0:
    return [1]
  tmp1 = str(stone)
  tmp2 = len(tmp1)
  if tmp2%2 == 0:
    return [int(tmp1[:tmp2//2]), int(tmp1[tmp2//2:])]
  return [stone*2024]

cache = {}
def evolve_times(stone, times):
  if times == 0:
    return 1

  if (stone, times) in cache:
    return cache[stone, times]

  result = 0
  tmp = evolve(stone)
  for s in tmp:
    result += evolve_times(s, times-1)
  cache[stone, times] = result
  return result

ans = 0
for stone in data:
  ans += evolve_times(stone,25)
print(ans)

ans = 0
for stone in data:
  ans += evolve_times(stone,75)
print(ans)
