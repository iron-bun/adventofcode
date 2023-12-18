#!/usr/bin/env python3

def valid(v, ranges):
  for desc, rules in ranges.items():
    for l, h in rules:
        if l <= v <= h:
            return True
  return False

def parse_rules(f):
    ranges = {}
    for line in f:
        line = line.strip()
        if line == "":
            break
        t, r = line.split(": ")
        r = r.split(" ")
        tmp = r[0].split("-")
        ranges[t] = [(int(tmp[0]), int(tmp[1]))]
        tmp = r[2].split("-")
        ranges[t].append((int(tmp[0]), int(tmp[1])))
    return ranges

def solution1(f):
    ranges = parse_rules(f)

    for line in f:
        line = line.strip()
        if line == "nearby tickets:":
            break

    ans = 0
    for line in f:
        line = line.strip()
        values = map(int, line.split(","))
        for v in values:
            if not valid(v, ranges):
                ans += v
    return ans

def solution2(f):
    rules = parse_rules(f)

    tickets = []
    for line in f:
        line = line.strip()
        if line in ("", "your ticket:", "nearby tickets:"):
          continue
        ticket = list(map(int, line.split(",")))
        for v in ticket:
          if not valid(v, rules):
            break
        else:
          tickets.append(ticket)

    potential_rules = []
    for idx in range(len(tickets[0])):
      valid_rules = []
      for desc, ranges in rules.items():
        for ticket in tickets:
          for l, h in ranges:
            if l <= ticket[idx] <= h:
              break
          else:
            break
        else:
          valid_rules.append(desc)
      potential_rules.append(valid_rules)

    while max([len(rule) for rule in potential_rules]) > 1:
      exclusive_rules = [rule[0] for rule in potential_rules if len(rule) == 1]
      for rule in potential_rules:
        if len(rule) == 1:
          continue
        for ex_rule in exclusive_rules:
          if ex_rule in rule:
            del rule[rule.index(ex_rule)]
    ans = 1
    for idx, rule in enumerate(potential_rules):
      if "departure" in rule[0]:
        ans *= tickets[0][idx]
    return ans


if __name__ == "__main__":
    with open("day16.txt") as f:
        print(solution1(f))
    with open("day16.txt") as f:
        print(solution2(f))
