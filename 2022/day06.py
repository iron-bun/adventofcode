#!/usr/bin/env python3

def solution1(data):
    return solution(data, 4)

def solution2(data):
    return solution(data, 14)

def solution(data, length):
    ans = length
    
    tmp = list(data[:length-1])
    data = data[length-1:]
    for char in data:
        tmp.append(char)
        if len(set(tmp)) == length:
            return ans
        tmp.pop(0)
        ans += 1
    return 0

if __name__ == "__main__":
    with open("day6.txt") as f:
        print(solution1(f.readline()))
    with open("day6.txt") as f:
        print(solution2(f.readline()))
