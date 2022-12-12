#!/usr/bin/env python3

import re

def solution1(data):
    ans = 0
    for line in data:
        line = line.strip()
        
        elf_1_start, elf_1_end, elf_2_start, elf_2_end = map(int ,re.split("[,-]",line))
        if elf_1_end - elf_1_start > elf_2_end - elf_2_start:
            elf_1_start, elf_1_end, elf_2_start, elf_2_end = elf_2_start, elf_2_end, elf_1_start, elf_1_end
        if elf_2_start <= elf_1_start and elf_2_end >= elf_1_end:
            ans += 1
            
    return ans

def solution2(data):
    ans = 0
    for line in data:
        line = line.strip()

        elf1, elf2 = [list(map(int, v.split("-"))) for v in line.split(",")]
        if not (elf1[1] < elf2[0] or elf2[1] < elf1[0]):
            ans += 1

    return ans
         
    
if __name__ == '__main__':
    with open("day4.txt") as f:
        print(solution1(f))
    with open("day4.txt") as f:
        print(solution2(f))
