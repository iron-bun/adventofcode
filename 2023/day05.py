#!/usr/bin/env python3

test_data = ["seeds: 79 14 55 13",
"",
"seed-to-soil map:",
"50 98 2",
"52 50 48",
"",
"soil-to-fertilizer map:",
"0 15 37",
"37 52 2",
"39 0 15",
"",
"fertilizer-to-water map:",
"49 53 8",
"0 11 42",
"42 0 7",
"57 7 4",
"",
"water-to-light map:",
"88 18 7",
"18 25 70",
"",
"light-to-temperature map:",
"45 77 23",
"81 45 19",
"68 64 13",
"",
"temperature-to-humidity map:",
"0 69 1",
"1 0 69",
"",
"humidity-to-location map:",
"60 56 37",
"56 93 4"]


items = []
new_items = []
processed = []

data = open("day05.txt")
for line in data:
  line = line.strip()

  if line[:5] == "seeds":
    items = line.split(" ")
    items = items[1:]
    items = list(map(int, items))
    continue

  if line == "":
    continue

  if line[-4:] == "map:":
    new_items += [i for i in items if i not in processed]
    items = new_items
    new_items = []
    processed = []
    continue

  maps = list(map(int, line.split()))
  for item in items:
    if item >= maps[1] and item < maps[1]+maps[2]:
      new_items.append(maps[0]+(item-maps[1]))
      processed.append(item)

new_items += [i for i in items if i not in processed]
print(min(new_items))
data.close()

items = {}
new_items = {}
processed = []
unprocessed = {}

data = open("day05.txt")
for line in data:
  line = line.strip()

  if line[:5] == "seeds":
    tmp = line.split(" ")
    tmp = tmp[1:]
    tmp = list(map(int, tmp))
    for t in zip(tmp[::2], tmp[1::2]):
      new_items[t[0]] = t[1]
    continue

  if line == "":
    continue

  if line[-4:] == "map:":
    for k, v in new_items.items():
      items[k] = v
    new_items = {}

    continue

  maps = list(map(int, line.split()))
  for k, v in items.items():
    item_start, item_end = k, k+v-1
    map_start, map_end = maps[1], maps[1]+maps[2]-1
    dest_start = maps[0]

    if item_start >= map_start and item_end <= map_end: #seeds fully in soil
      new_items[dest_start+(item_start - map_start)] = v

    elif item_start < map_start and item_end > map_end: #soil fully in seed
      unprocessed[item_start] = map_start - item_start
      new_items[dest_start] = maps[2]
      unprocessed[map_end+1] = item_end - map_end

    elif item_start < map_start and item_end >= map_start: #items partly contains the low end of map
      unprocessed[item_start] = map_start - item_start
      new_items[dest_start] = item_end - map_start + 1

    elif item_start >= map_start and item_start <= map_end and item_end > map_end: #partly contained high
      new_items[dest_start+(item_start-map_start)] = map_end - item_start + 1
      unprocessed[map_end+1] = item_end - map_end
    else: #items unrelated to this map
      unprocessed[k] = v

  items = unprocessed
  unprocessed = {}
print(min(items.keys()))
data.close()
