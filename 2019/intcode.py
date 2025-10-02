
def peek(program, idx, mode):
    if mode == "1":
        return program[idx]
    else:
        return program[program[idx]]

def poke(program, idx, mode, value):
    if mode == "1":
        program[idx] = value
    else:
        program[program[idx]] = value

def add(program, program_input, idx, modes):
    v1 = peek(program, idx+1, modes[2])
    v2 = peek(program, idx+2, modes[1])
    poke(program, idx+3, modes[0], v1 + v2)
    return idx+4

def mult(program, program_input, idx, modes):
    v1 = peek(program, idx+1, modes[2])
    v2 = peek(program, idx+2, modes[1])
    poke(program, idx+3, modes[0], v1 * v2)
    return idx+4

def read(program, program_input, idx, modes):
    poke(program, idx+1, modes[0], program_input)
    return idx+2

def write(program, program_input, idx, modes):
    print(peek(program, idx+1, modes[0]))
    return idx+2

def jit(program, program_input, idx, modes):
    v1 = peek(program, idx+1, modes[1])
    if v1 != 0:
        return peek(program, idx+2, modes[0])
    else:
        return idx+3

def jif(program, program_input, idx, modes):
    v1 = peek(program, idx+1, modes[1])
    if v1 == 0:
        return peek(program, idx+2, modes[0])
    else:
        return idx+3

def lt(program, program_input, idx, modes):
    v1 = peek(program, idx+1, modes[2])
    v2 = peek(program, idx+2, modes[1])
    if v1 < v2:
        poke(program, idx+3, modes[0], 1)
    else:
        poke(program, idx+3, modes[0], 0)
    return idx+4

def eq(program, program_input, idx, modes):
    v1 = peek(program, idx+1, modes[2])
    v2 = peek(program, idx+2, modes[1])
    if v1 == v2:
        poke(program, idx+3, modes[0], 1)
    else:
        poke(program, idx+3, modes[0], 0)
    return idx+4

commands = {1: (add, 3), 2:(mult, 3), 3:(read,1), 4:(write,1), 5:(jit, 2), 6:(jif, 2), 7:(lt, 3), 8:(eq,3)}

def run(program, program_input=None):
    idx = 0
    while True:
        if program[idx] == 99:
            break
        instruction = int(program[idx]%100)
        if instruction not in commands:
            print(f"unknown instruction {program[idx]} at {idx}")
            exit()

        args = commands[instruction]
        idx = args[0](program, program_input, idx, f"{program[idx]:0{args[1]+2}d}")

    return program

