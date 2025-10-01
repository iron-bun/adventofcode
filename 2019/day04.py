#!/usr/bin/env python3

def gen_candidates(start, end):
    start_values = str(start)

    while int(start_values) < end:
        tmp = start_values[0]
        i = start_values[0]
        for j in start_values[1:]:
          if j < i:
            tmp += i
          else:
            tmp += j
            i = j
        start_values = tmp
        if int(start_values) > end:
            break
        yield start_values
        start_values = str(int(start_values) + 1)

ans = 0
for i in gen_candidates(248345, 746315):
    for j, k in zip(i, i[1:]):
      if j == k:
        ans += 1
        break
print(ans)

ans = 0
for i in gen_candidates(248345, 746315):
    groups = []
    length = 1
    tmp = i[0]
    for j in range(1,6):
      if i[j] == tmp:
        length+=1
      else:
        groups.append(length)
        tmp = i[j]
        length = 1
    groups.append(length)
    if 2 in groups:
      ans += 1
print(ans)
