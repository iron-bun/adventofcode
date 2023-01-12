#!/usr/bin/env python3


def apply_value_mask(value, mask):
    zeros = int("".join(["1" if v != "0" else "0" for v in mask]), 2)
    ones  = int("".join(["0" if v != "1" else "1" for v in mask]), 2)

    value = value & zeros
    value = value | ones

    return value

def solution1(f):
    memory = {}

    for line in f:
        line = line.strip()

        if line[:4] == "mask":
            mask = line.split(" ")[2]
        else:
            tmp = line.index("]")
            addr = int(line[4:tmp])
            val = int(line.split(" ")[2])

            memory[addr] = apply_value_mask(val, mask)

    return sum(memory.values())

def apply_floating_addresses(addr, mask):

    if "X" not in mask:
        ones = int("".join(["1" if v == "1" else "0" for v in mask]), 2)
        addr = int("".join(addr), 2)

        yield addr | ones

    else:
        mask = mask[:]

        tmp = mask.index("X")
        mask[tmp] = "0"

        addr[tmp] = "0"
        yield from apply_floating_addresses(addr, mask)

        addr[tmp] = "1"
        yield from apply_floating_addresses(addr, mask)

def apply_memory_mask(addr, mask):
    yield from apply_floating_addresses(addr, mask)
    
def solution2(f):
    memory = {}
    
    for line in f:
        line = line.strip()

        if line[:4] == "mask":
            mask = list(line.split(" ")[2])
        else:
            tmp = line.index("]")
            addr = int(line[4:tmp])
            addr = list(f"{addr:036b}")
            val = int(line.split(" ")[2])

            for a in apply_memory_mask(addr, mask):
                memory[a] = val

    return sum(memory.values())

if __name__ == "__main__":
    with open("day14.txt") as f:
        print(solution1(f))
    with open("day14.txt") as f:
        print(solution2(f))
