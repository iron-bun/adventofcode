#!/usr/bin/env python3

links = {}
with open("day23.txt") as f:
    for line in f:
        a, b = line.strip().split("-")
        a, b = sorted((a,b))
        if a not in links:
            links[a] = set()
        if b not in links:
            links[b] = set()
        links[a].add(b)
        links[b].add(a)

ans_1 = 0
for i, k in enumerate(sorted(links.keys())):
    links[k] = sorted(links[k])
    for idx, a in enumerate(links[k]):
        if a <= k:
            continue
        for b in links[k][idx+1:]:
            if b in links[a]:
                if "t" in (k[0], a[0], b[0]):
                    ans_1 += 1
print(ans_1)

networks = []
for k in links.keys():
    for n in networks:
        for node in n:
            if node not in links[k]:
                break
        else:
            networks.append(n+[k])
    networks.append([k])

ans = None
len_ans = None
for n in networks:
    if len_ans == None or len(n) > len_ans:
        len_ans = len(n)
        ans = ",".join(sorted(n))
print(ans)

