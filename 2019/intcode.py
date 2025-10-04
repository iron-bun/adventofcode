
class Intcode:
    def __init__(self, stdin, stdout, prog):
        self.stdin = stdin
        self.stdout = stdout
        self.prog = prog
        self.idx = 0
        self.commands = {1: (self.add, 3), 2:(self.mult, 3), 3:(self.read,1), 4:(self.write,1), 5:(self.jit, 2), 6:(self.jif, 2), 7:(self.lt, 3), 8:(self.eq,3)}

    def peek(self, idx, mode):
        if mode == "1":
            return self.prog[idx]
        else:
            return self.prog[self.prog[idx]]

    def poke(self, idx, mode, value):
        if mode == "1":
            self.prog[self.idx] = value
        else:
            self.prog[self.prog[idx]] = value

    def add(self, modes):
        v1 = self.peek(self.idx+1, modes[2])
        v2 = self.peek(self.idx+2, modes[1])
        self.poke(self.idx+3, modes[0], v1 + v2)
        self.idx+=4

    def mult(self, modes):
        v1 = self.peek(self.idx+1, modes[2])
        v2 = self.peek(self.idx+2, modes[1])
        self.poke(self.idx+3, modes[0], v1 * v2)
        self.idx+=4

    def read(self, modes):
        self.poke(self.idx+1, modes[0], self.stdin.get())
        self.idx+=2

    def write(self, modes):
        self.stdout.put(self.peek(self.idx+1, modes[0]))
        self.idx+=2

    def jit(self, modes):
        v1 = self.peek(self.idx+1, modes[1])
        if v1 != 0:
            self.idx = self.peek(self.idx+2, modes[0])
        else:
            self.idx+=3

    def jif(self, modes):
        v1 = self.peek(self.idx+1, modes[1])
        if v1 == 0:
            self.idx = self.peek(self.idx+2, modes[0])
        else:
            self.idx+=3

    def lt(self, modes):
        v1 = self.peek(self.idx+1, modes[2])
        v2 = self.peek(self.idx+2, modes[1])
        if v1 < v2:
            self.poke(self.idx+3, modes[0], 1)
        else:
            self.poke(self.idx+3, modes[0], 0)
        self.idx+=4

    def eq(self, modes):
        v1 = self.peek(self.idx+1, modes[2])
        v2 = self.peek(self.idx+2, modes[1])
        if v1 == v2:
            self.poke(self.idx+3, modes[0], 1)
        else:
            self.poke(self.idx+3, modes[0], 0)
        self.idx+=4


    def run(self):
        while True:
            if self.prog[self.idx] == 99:
               break
            instruction = int(self.prog[self.idx]%100)
            if instruction not in self.commands:
                print(f"unknown instruction {program[idx]} at {idx}")
                exit()

            args = self.commands[instruction]
            args[0](f"{self.prog[self.idx]:0{args[1]+2}d}")

        return self.prog

