#!/usr/bin/env python3

with open("day03.txt") as f:
    banks = f.readlines()

def find_jolt(bank, multiplier):
    if multiplier == 0:
        return int(max(bank))
    else:
        max_digit = max(bank[:-1*multiplier])
        idx = bank.index(max_digit)
        return int(max_digit)*10**multiplier + find_jolt(bank[idx+1:], multiplier-1)

ans = 0
for bank in banks:
    ans += find_jolt(bank.strip(), 1)
print(ans)

ans = 0
for bank in banks:
    ans += find_jolt(bank.strip(), 11)
print(ans)

