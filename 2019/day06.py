#!/usr/bin/env python3

def score(orbits, obj, points):
    you, san = False, False
    orbits[obj][0] = points

    for o in orbits[obj][1]:
      tmp1, tmp2 = score(orbits, o, points+1)
      you = you or tmp1
      san = san or tmp2
      if o == "YOU":
        you = True
      if o == "SAN":
        san = True

    orbits[obj][2] = you
    orbits[obj][3] = san

    return you, san

orbits = {"COM":[0, [], False, False]}
with open("day06.txt") as f:
  for line in f:
    host, sat = line.strip().split(")")

    if host not in orbits:
      orbits[host] = [0,[], False, False]
    if sat not in orbits:
      orbits[sat] = [0,[], False, False]

    orbits[host][1].append(sat)

score(orbits, "COM", 0)

you_obj_points = 0
san_obj_points = 0
max_shared_points = 0
max_shared_obj = "COM"

ans = 0
for o in orbits:
    ans += orbits[o][0]

    if "YOU" in orbits[o][1]:
      you_obj_points = orbits[o][0]
    if "SAN" in orbits[o][1]:
      san_obj_points = orbits[o][0]
    if orbits[o][2] and orbits[o][3] and orbits[o][0] > max_shared_points:
      max_shared_points = orbits[o][0]
      max_shared_obj = o

print(ans)
print(you_obj_points + san_obj_points - max_shared_points * 2)
