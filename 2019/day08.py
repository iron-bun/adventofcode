#!/usr/bin/env python3

with open("day08.txt") as f:
  data = f.read().strip()

layers = [data[x:x+150] for x in range(0,len(data),150)]

ans = None
min_zeros = None
for l in layers:
    tmp = [0 for v in l if v == "0"]
    if min_zeros == None or len(tmp) < min_zeros:
        min_zeros = len(tmp)
        ones = [1 for v in l if v == "1"]
        twos = [2 for v in l if v == "2"]
        ans = len(ones) * len(twos)
print(ans)

ans = ["2"]*150
for l in layers:
    tmp = [b if a == "2" else a for a,b in zip(ans,l)]
    ans = tmp

for i in range(6):
   print("".join("*" if a == "1" else " " for a in ans[i*25:i*25+25]))
