#!/usr/bin/env python3

from math import copysign

moves = {"R":(1,0), "U":(0,1), "L":(-1, 0), "D":(0,-1)}

def sign(a):
    if a == 0:
        return 0
    else:
        return copysign(1, a)

def elementwise_add(a, b):
    return tuple(i+j for i,j in zip(a, b))

def process_commands(data, rope):
    short_tail_trail = set()
    long_tail_trail = set()
    
    for line in data:
        line = line.strip()
        command, distance = line.split(" ")
        command = moves[command]
        distance = int(distance)
        
        for _ in range(distance):
            rope[0] = elementwise_add(rope[0], command)
            
            for idx in range(len(rope)-1):
                head, tail = rope[idx], rope[idx+1]
                
                if abs(head[0] - tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
                    break
                
                segment_command = (sign(i-j) for i, j in zip(head, tail))
                tail = elementwise_add(tail, segment_command)
                rope[idx+1] = tail
                
            short_tail_trail.add(rope[1])
            long_tail_trail.add(rope[9])
            
    return len(short_tail_trail), len(long_tail_trail)


if __name__ == "__main__":
    with open("day9.txt") as f:
        print(process_commands(f,  [(0,0)] * 10))
