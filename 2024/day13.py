#!/usr/bin/env python3
import re
from operator import mul

def get_games(file):
    while True:
      tmp = f.readline()
      if tmp == "":
        break
      button_a = re.findall("(\d+)", tmp)

      tmp = f.readline()
      button_b = re.findall("(\d+)", tmp)

      tmp = f.readline()
      prize = re.findall("(\d+)", tmp)
      prize = tuple(map(int,prize))
      prize_pt2 = (prize[0] + 10000000000000, prize[1]+10000000000000)

      f.readline()

      yield tuple(map(int,button_a)), tuple(map(int,button_b)), prize, prize_pt2

def solve_game(game):
  gx, gy = game[2]

  b1, a1 = game[0]
  b1 *= -1
  c1 = 0

  b2, a2 = game[1]
  b2 *= -1
  c2 = a2*gx + b2*gy
  c2 *= -1

  if            (b1*c2) %  (a1*b2 - a2*b1)==0 and (0 - c2*a1)% (a1*b2 - a2*b1)==0:
    intercept = (b1*c2) // (a1*b2 - a2*b1),       (0 - c2*a1)//(a1*b2 - a2*b1)
    buttonA = intercept[1]/a1
    buttonB = (gy-intercept[1])/a2
    if int(buttonA) == buttonA and int(buttonB) == buttonB:
      buttonA = int(buttonA)
      buttonB = int(buttonB)
      return buttonA*3 + buttonB
  return 0

f = open("day13.txt")
ans_1 = 0
ans_2 = 0
for game in get_games(f):
  ans_1 += solve_game((game[0], game[1], game[2]))
  ans_2 += solve_game((game[0], game[1], game[3]))

print(ans_1)
print(ans_2)
