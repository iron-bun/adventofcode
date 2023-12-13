#!/usr/bin/env python3

def solution1(f):
    start_time = int(f.readline())
    timetable = f.readline().split(",")

    bus = None
    tmp = None

    for b in timetable:
        if b == "x":
            continue
        b = int(b)
        
        if tmp == None:
            bus = b
            tmp = b-start_time%b
        elif tmp > b-start_time%b:
            bus = b
            tmp = b-start_time%b

    return bus*tmp
        
def solution2(f):
    f.readline()
    timetable = f.readline().strip().split(",")

    timetable = {int(o):int(t) for o,t in enumerate(timetable) if t != "x"}

    step = 1
    ans = 1

    for idx in sorted(timetable.keys()):
      while (ans+idx) % timetable[idx] != 0:
        ans += step
      step *= timetable[idx]

    return ans
    
if __name__ == "__main__":
    with open("day13.txt") as f:
        print(solution1(f))

    with open("day13.txt") as f:
        print(solution2(f))
