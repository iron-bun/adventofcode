#!/usr/bin/env python3

def find_candidates(target, operands, operators):
  if len(operands) == 1:
    yield operands[0]
  else:
    tmp = operands[-1]
    for v in find_candidates(target, operands[:-1], operators):
      if v > target:
        yield v
      else:
        for o in operators:
          yield o(tmp, v)

def find_valid_targets(target, operands, operators):
  for v in find_candidates(target, operands, operators):
    if v == target:
      return target
  return 0

ans_1 = 0
ans_2 = 0
with open("day07.txt") as f:
  for line in f:
    line = line.strip()
    target, operands = line.split(":")
    operands = operands.split()

    target = int(target)
    operands = list(map(int, operands))

    ans_1 += find_valid_targets(target, operands, [lambda a, b: a+b, lambda a, b: a*b])
    ans_2 += find_valid_targets(target, operands, [lambda a, b: a+b, lambda a, b: a*b, lambda a,b: int(str(b)+str(a))])
print(ans_1)
print(ans_2)
