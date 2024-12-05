#!/usr/bin/env python3

with open("day05.txt") as f:
  rules = []
  for line in f:
    line = line.strip()
    if line == "":
      break
    rules.append(line.split("|"))

  data = []
  for line in f:
    line = line.strip()
    data.append(line.split(","))

def test_valid(update, rules):
  valid = True
  for rule in rules:
    if rule[0] not in update:
      continue
    if rule[1] not in update:
      continue
    if update.index(rule[0]) > update.index(rule[1]):
      valid = False
      break
  return valid

ans = 0
for update in data:
  if test_valid(update, rules):
      ans += int(update[(len(update)-1)//2])
print(ans)

ans = 0
for update in data:
  if test_valid(update, rules):
    continue
  while not test_valid(update, rules):
    for rule in rules:
      if rule[0] not in update:
        continue
      if rule[1] not in update:
        continue
      p1, p2 = update.index(rule[0]), update.index(rule[1])
      if p1 > p2:
        update = update[0:p2] + [rule[0]] + update[p2:p1] + update[p1+1:]
  ans += int(update[(len(update)-1)//2])
print(ans)
