#!/usr/bin/env python3

testdata = ["19, 13, 30 @ -2, 1, -2",
"18, 19, 22 @ -1, -1, -2",
"19, 13, 30 @ -2, 1, -2",
"20, 19, 15 @ 1, -5, -3",
"18, 19, 22 @ -1, -1, -2",
"20, 25, 34 @ -2, -2, -4"]

def parse(line):
  tmp = line.strip().split("@")
  pos = list(map(int, tmp[0].split(",")))
  vec = list(map(int, tmp[1].split(",")))
  return pos + vec

def get_c(a):
  return a[1] - a[0]*a[4]/a[3]

def check_intersection(a, b):
  px1, py1, pz1, vx1, vy1, vz1 = a
  px2, py2, pz2, vx2, vy2, vz2 = b
  m1, m2 = vy1/vx1*-1, vy2/vx2*-1
  c1, c2 = get_c(a)*-1, get_c(b)*-1

  try: 
    ix, iy = (c2-c1)/(m1-m2), (m2*c1-m1*c2)/(m1-m2)
  except:
    return False

  if (iy-py1)/vy1 > 0 and (iy-py2)/vy2 > 0 and 200000000000000 <= ix <= 400000000000000 and 200000000000000 <= iy <= 400000000000000:
    return True
  return False

ans = 0
with open("day24.txt") as f:
  lines = f.readlines()
  for i, line1 in enumerate(lines):
    for line2 in lines[i+1:]:
      if check_intersection(parse(line1), parse(line2)):
        ans += 1
print(ans)
