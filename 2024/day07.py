#!/usr/bin/env python3

from operator import add, mul

operators = [add, mul, lambda a,b: int(str(a)+str(b))]

def convert_to_base(value, base, length):
    if value == 0:
        return [0]*length
    digits = []
    while value:
        digits.append(int(value % base))
        value //= base
    return [0] * (length-len(digits)) + digits[::-1]

def find_valid_targets(target, operands, operators):
  base = len(operators)
  for i in range(len(operators)**(len(operands)-1)):
        tmp = operands[0]
        for o,op in enumerate(convert_to_base(i, len(operators), len(operands)-1)):
          tmp = operators[op](tmp, operands[o+1])
        if tmp == target:
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

    ans_1 += find_valid_targets(target, operands, operators[:-1])
    ans_2 += find_valid_targets(target, operands, operators)
print(ans_1)
print(ans_2)
