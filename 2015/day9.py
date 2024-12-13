#!/usr/bin/env python3

import itertools

def find_shortest(locations, flights):
    ans_1, ans_2 = None, None
    
    for route in itertools.permutations(locations):
      prev = route[0]
      tmp = 0
      for stop in route[1:]:
        stage = tuple(sorted((prev,stop)))
        tmp += flights[stage]
        prev = stop
      else:
        if ans_1 == None or tmp < ans_1:
          ans_1 = tmp
        if ans_2 == None or tmp > ans_2:
          ans_2 = tmp
    return ans_1, ans_2

def solution(f):
    locations = set()
    flights = {}
    for line in f:
        line = line.strip().split(" ")
        
        depart, dest = sorted((line[0], line[2]))
        locations.add(depart)
        locations.add(dest)
        flights[(depart,dest)] = int(line[4])

    return find_shortest(locations, flights)
        
if __name__ == "__main__":
    with open("data/day9.txt") as f:
        print(solution(f))

#431 too high
