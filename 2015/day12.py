#!/usr/bin/env python3

import json

file = json.load(open("data/day12.txt"))

def parse_list(data, red=False):
  for item in data:
    yield from parse_item(item, red)

def parse_dict(data, red=False):
  total = 0
  for k, v in data.items():
    if red and (k == "red" or v == "red"):
      return 0
    for i in parse_item(k, red):
      total += i
    for i in parse_item(v, red):
      total += i
  yield total

def parse_item(data, red=False):
  if type(data) == int:
    yield data
  elif type(data) == list:
    yield from parse_list(data, red)
  elif type(data) == dict:
    yield from parse_dict(data, red)

total = 0
for v in parse_item(file):
  total += v
print(total)


total = 0
for v in parse_item(file, True):
  total += v
print(total)
