#!/usr/bin/env python3

test_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]


def game_generator(data):
  for line in data:
    line = line.strip()
    game = {}

    tmp = line.split(":")

    game["id"] = int(tmp[0][5:])
    
    game["rounds"] = []
    rounds = tmp[1].split(";")
    for r in rounds:
        result = {"r":0, "b":0, "g":0}
        cubes = r.split(",")
        for cube in cubes:
            if cube[-4:]=="blue":
                result["b"] = int(cube[:-4])
            if cube[-5:]=="green":
                result["g"] = int(cube[:-5])
            if cube[-3:]=="red":
                result["r"] = int(cube[:-3])
        game["rounds"].append(result)
    yield game

def validate_game(game, r_max, g_max, b_max):
    for r in game["rounds"]:
        if r["r"] > r_max or r["g"] > g_max or r["b"] > b_max:
            return False
    return True

ans = 0
with open("day02.txt") as data:
  for g in game_generator(data):
      if validate_game(g, 12, 13, 14):
          ans += g["id"]
print(ans)

ans = 0
with open("day02.txt") as data:
  for game in game_generator(data):
    r, g, b = 0, 0, 0
    for turn in game["rounds"]:
       if turn["r"] > r:
          r = turn["r"]
       if turn["g"] > g:
          g = turn["g"]
       if turn["b"] > b:
          b = turn["b"]
    power = r*g*b
    ans += power
print(ans)
