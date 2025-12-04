#!/usr/bin/env python3

ingredients = []
with open("data/day15.txt") as f:
  for line in f:
    line = line.strip()
    ingredient, properties = line.split(":")
    properties = properties.split(",")
    properties = list(map(lambda x: int(x.split(" ")[2]), properties))
    ingredients.append(properties)

ans = 0
for i in range(1, 101):
  for j in range(1, 101-i):
    for k in range(1, 101-i-j):
        l = 100 - i - j - k
        tmp1 = (i,j,k,l)
        tmp2 = 1
        for m in range(4):
          tmp3 = 0
          for n in range(4):
            tmp4 = ingredients[n][m]*tmp1[n]
            tmp3 += tmp4
          if tmp3 <= 0:
            tmp2 = 0
            break
          tmp2 *= tmp3
        if tmp2 > ans:
          ans = tmp2
print(ans)

ans = 0
for i in range(1, 101):
  for j in range(1, 101-i):
    for k in range(1, 101-i-j):
        l = 100 - i - j - k
        tmp1 = (i,j,k,l)
        if sum(ingredients[i][4]*tmp1[i] for i in range(4)) != 500:
          continue
        tmp2 = 1
        for m in range(4):
          tmp3 = 0
          for n in range(4):
            tmp4 = ingredients[n][m]*tmp1[n]
            tmp3 += tmp4
          if tmp3 <= 0:
            tmp2 = 0
            break
          tmp2 *= tmp3
        if tmp2 > ans:
          ans = tmp2
print(ans)
