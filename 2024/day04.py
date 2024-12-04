#!/usr/bin/env python3

test_data = ["MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]

with open("day04.txt") as f:
  test_data = f.readlines()

letters = {}

for i,line in enumerate(test_data):
  for j,char in enumerate(line):
    letters[j,i] = char

def tadd(a, b):
  return tuple(map(sum, zip(a,b)))

directions = [(-1,-1), (0,-1), (1, -1),
              (-1, 0),         (1, 0),
              (-1, 1), (0, 1), (1, 1)]
ans = 0
for d in directions:
  for k in letters.keys():
    if letters[k] == "X":
      k = tadd(k, d)
      if letters.get(k, None) == "M":
        k = tadd(k, d)
        if letters.get(k, None) == "A":
          k = tadd(k, d)
          if letters.get(k, None) == "S":
            ans += 1
print(ans)


directions = [
               ((-1,-1), (1, 1)),
               ((-1, 1), (1, -1)),
               ((1, 1), (-1, -1)),
               ((1, -1), (-1, 1))
             ]
ans = 0
for k in letters.keys():
  if letters[k] == "A":
     tmp = 0
     for d in directions:
       if letters.get(tadd(k, d[0])) == "M" and letters.get(tadd(k, d[1])) == "S":
         tmp += 1
     if tmp == 2:
       ans += 1
print(ans)
