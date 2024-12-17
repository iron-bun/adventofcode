#!/usr/bin/env python3

import re

def combo_operand(value):
    if value in (0,1,2,3):
        return value
    if value in (4,5,6):
        return registers[value-4]
    if value == 7:
        print("invalid combo operand")
        exit()

def adv(value):
    registers[0] = int(registers[0]/2**combo_operand(value))

def bxl(value):
    registers[1] = registers[1] ^ value

def bst(value):
    registers[1] = combo_operand(value)%8
    
def jnz(value):
    global ptr
    if registers[0] == 0:
        return
    ptr = value - 2

def bxc(value):
    registers[1] = registers[1] ^ registers[2]

output_buffer = []
def out(value):
    output_buffer.append(str(combo_operand(value)%8))

def bdv(value):
    registers[1] = int(registers[0]/2**combo_operand(value))

def cdv(value):
    registers[2] = int(registers[0]/2**combo_operand(value))

operators = {"0":adv, "1":bxl, "2":bst, "3":jnz, "4":bxc, "5":out, "6":bdv, "7":cdv}
registers = []
ptr = 0

with open("day17.txt") as f:
    for line in f:
        if line.strip() == "":
            break
        registers.append(int(re.findall("(\d+)", line)[0]))

    instructions = re.findall("\d+", f.readline())

while ptr >= 0 and ptr < len(instructions):
    op, operand = instructions[ptr:ptr+2]
    operators[op](int(operand))
    ptr += 2

#part 1    
print(output_buffer)

ans = 0

prev = 0
i = 169103670287
idx = 0
inc = """10223616
51529383936
10223616
381402152960
65536
8323072
65536
524288
125239296
65536
68719411200
65536
597705883648""".split("\n")
inc = tuple(map(int, inc))

while True:
    ptr = 0
    output_buffer = []
    registers = [8**15+i, 0, 0]
    init = registers[0]
    
    while ptr >= 0 and ptr < len(instructions):
        op, operand = instructions[ptr:ptr+2]
        operators[op](int(operand))
        ptr += 2

    if output_buffer == instructions:
        ans = init
        break

    i += inc[idx]
    idx += 1
    idx %= len(inc)


print(ans)

