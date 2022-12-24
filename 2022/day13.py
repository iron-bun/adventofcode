#!/usr/bin/env python3
from functools import cmp_to_key

def compare_packet(left, right):
    cmp = 0
    idx = -1
    
    while cmp == 0:
        idx += 1
        if idx == len(left) and idx == len(right):
            break
        elif idx >= len(left):
            cmp = -1
            break
        elif idx >= len(right):
            cmp = 1
            break
        
        a, b = left[idx], right[idx]
        
        if type(a) == int and type(b) == int:
            if a < b:
                cmp = -1
            elif a > b:
                cmp = 1
        elif type(a) == list and type(b) == list:
            cmp = compare_packet(a, b)
        elif type(a) == int and type(b) == list:
            cmp = compare_packet([a], b)
        else:
            cmp = compare_packet(a, [b])
            
    return cmp
        
def solution1(data):
    ans = 0
    idx =0
    
    line = f.readline()
    while line:
        left = eval(line)
        right = eval(f.readline())
        idx += 1
        
        if compare_packet(left, right) == -1:
            ans += idx
        
        f.readline()
        line = f.readline()
        
    return ans
    
def solution2(data):
    lines = []
    for line in data:
        if line == "\n":
            continue
        lines.append(line.strip())
    lines.append("[[2]]")
    lines.append("[[6]]")
    
    lines = map(eval, lines)
    
    lines = sorted(lines, key=cmp_to_key(compare_packet))
    
    ans = lines.index([[2]]) + 1
    ans *= lines.index([[6]]) + 1
    return ans
    
if __name__ == "__main__":
    with open("day13.txt") as f:
        print(solution1(f))
    with open("day13.txt") as f:
        print(solution2(f))
