#!/usr/bin/env python3

def run(program):
    idx = 0
    while True:
        if program[idx] == 99:
            break
        elif program[idx] == 1:
            v1 = program[program[idx+1]]
            v2 = program[program[idx+2]]
            program[program[idx+3]] = v1 + v2
        elif program[idx] == 2:
            v1 = program[program[idx+1]]
            v2 = program[program[idx+2]]
            program[program[idx+3]] = v1 * v2
        else:
            print(f"unknown instruction {program[idx]} at {idx}")
            exit()
        idx += 4
    return program

with open("day02.txt") as f:
    line = f.readline().strip().split(",")
    line = list(map(int, line))

    p = line.copy()
    p[1] = 12
    p[2] = 2
    p = run(p)
    print(p[0])

    found = False
    for noun in range(99):
        for verb in range(99):

            p = line.copy()
            p[1] = noun
            p[2] = verb

            run(p)
            if p[0] == 19690720:
                print(noun*100 + verb)
                found = True
                break
        if found:
            break
