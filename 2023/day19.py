#!/usr/bin/env python3

from copy import deepcopy

def parse_workflows(data):
    workflows = {}
    for line in data:
        line = line.strip()
        if line == "":
            return workflows
        rule_name = line[:line.index("{")]
        rules = line[line.index("{")+1:-1].split(",")
        workflows[rule_name] = rules
    return workflows

def apply_workflow(part, workflow):
    for w in workflow:
        if "<" not in w and ">" not in w:
            return w
        field = w[0]
        comp = w[1]
        value = int(w[2:w.index(":")])
        dest = w[w.index(":")+1:]
        if comp == ">" and part[field] > value:
            return dest
        if comp == "<" and part[field] < value:
            return dest

def process_part(part, workflows):
    part = part[1:-1].split(",")
    tmp = {}
    for p in part:
        tmp[p[0]] = int(p[2:])
    part = tmp

    workflow = "in"
    while True:
        if workflow == "A":
            return part.get("x", 0) + part.get("m", 0) + part.get("a", 0) + part.get("s")
        elif workflow == "R":
            return 0
        else:
            workflow = apply_workflow(part, workflows[workflow])

with open("day19.txt") as f:
    ans = 0
    workflows = parse_workflows(f)
    for part in f:
        ans += process_part(part.strip(), workflows)
    print(ans)

def split_parts(part, steps, workflows):
    result = {}
    for idx, step in enumerate(workflows[steps]):
      if "<" not in step and ">" not in step:
        result[step] = part
        return result

      field = step[0]
      comp = step[1]
      value = int(step[2:step.index(":")])
      dest = step[step.index(":")+1:]
      if dest == "A":
        dest += str(idx)

      if comp == "<":
          if part[field][0] >= value:
              pass
          elif part[field][1] < value:
              result[dest] = part
              return result
          else:
              tmp = deepcopy(part)
              tmp[field][1] = value - 1
              result[dest] = tmp
              part[field][0] = value
      else:
          if part[field][1] <= value:
              pass
          elif part[field][0] > value:
              result[dest] = part
              return result
          else:
              tmp = deepcopy(part)
              tmp[field][0] = value + 1
              result[dest] = tmp
              part[field][1] = value

def calculate_workflows(parts, workflows):
    accepted_parts = []
    while len(parts) > 0:
        tmp2 = {}
        for flow, part in parts.items():
                tmp = split_parts(part, flow, workflows)
                for k, v in tmp.items():
                    if k[0] == "A":
                        accepted_parts.append(v)
                        continue
                    if k != "R":
                        tmp2[k] = v
        parts = tmp2
    return accepted_parts

ans = 0
parts = {"in":{"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}}
parts = calculate_workflows(parts, workflows)
for part in parts:
    ans += (part["x"][1]-part["x"][0]+1) * (part["m"][1]-part["m"][0]+1) * (part["a"][1]-part["a"][0]+1) * (part["s"][1]-part["s"][0]+1)

print(ans)
