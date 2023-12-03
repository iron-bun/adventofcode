#!/usr/bin/env python3

import hashlib

def puzzle(prefix):

    key = "bgvyzdsv"
    suffix = 1
    while True:
        guess = hashlib.md5((key+str(suffix)).encode()).hexdigest()
        if guess[:len(prefix)] == prefix:
            break
        suffix += 1
    return suffix

def part1():
    return puzzle("00000")

def part2():
    return puzzle("000000")

if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
