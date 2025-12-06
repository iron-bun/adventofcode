#!/usr/bin/env python3

transitions = {}
with open("data/day19.txt") as f:
  for line in f:
    line = line.strip()

    if line == "":
      break

    atom, result = line.split(" => ")
    if atom not in transitions:
      transitions[atom] = []
    transitions[atom].append(result)

  start = f.readline().strip()

results = set()
for k in transitions.keys():
  for idx in range(len(start)):
    if k == start[idx:idx+len(k)]:
      for transition in transitions[k]:
        results.add(start[:idx]+transition+start[idx+len(k):])
print(len(results))


tmp = {}
for k in transitions.keys():
  for v in transitions[k]:
    if v not in tmp:
      tmp[v] = []
    tmp[v].append(k)
transitions = tmp
keys = sorted(transitions.keys(), reverse=True, key=lambda x: len(x))

def compress(string, depth):

  if string=="e":
    return depth

  for k in keys:
    for idx in range(len(string)):
      if k == string[idx:idx+len(k)]:
        for transition in transitions[k]:
          tmp = compress(string[:idx]+transition+string[idx+len(k):], depth+1)
          if tmp != 0:
            return tmp
  return 0

print(compress(start,0))
