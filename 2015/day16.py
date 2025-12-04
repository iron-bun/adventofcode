#!/usr/bin/env python3

ticker_tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split("\n")

attributes = {}
for line in ticker_tape:
  category, value = line.split(":")
  attributes[category] = int(value)

with open("data/day16.txt") as f:
  for line in f:
    line = line.strip()
    idx = line.index(":")
    details = line[idx+1:].split(",")
    for detail in details:
       detail = detail.split(":")
       if attributes[detail[0].strip(" ")] != int(detail[1]):
         break
    else:
      print(line[:idx])

import operator
comparitors = {"cats": operator.gt,
        "pomeranians": operator.lt,
           "goldfish": operator.lt,
              "trees": operator.gt}

with open("data/day16.txt") as f:
  for line in f:
    line = line.strip()
    idx = line.index(":")
    details = line[idx+1:].split(",")
    for detail in details:
       detail = detail.split(":")
       if not comparitors.get(detail[0].strip(), operator.eq)(int(detail[1]), attributes[detail[0].strip(" ")]):
         break
    else:
      print(line[:idx])
