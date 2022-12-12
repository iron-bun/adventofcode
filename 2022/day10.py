#!/usr/bin/env python3

class cpu:
    def __init__(self):
        self.clock = 0
        self.x = 1
        self.signal = 0
        
    def tick(self):
        if -2 < (self.clock%40) - self.x < 2:
            print("#", end="")
        else:
            print(" ", end="")
         
        self.clock += 1
        
        if self.clock%40 == 0:
            print()
            
        if self.clock in [20, 60, 100, 140, 180, 220]:
            self.signal += self.clock * self.x
        
    def add(self, value):
        self.tick()
        self.tick()
        self.x += int(value)

def solution(data):
    tmp = cpu()
    for line in data:
        line = line.strip()
        command = line.split(" ")
        
        if command[0] == "noop":
            tmp.tick()
        elif command[0] == "addx":
            tmp.add(int(command[1]))
            
    return tmp.signal
    
if __name__ == '__main__':
    with open("day10.txt") as f:
        print(solution(f))
