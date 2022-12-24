#!/usr/bin/env python3

OK = 0
GUARDED = 1
BLOCKED = 2

class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.move = False

    def propose(self, old_data, new_data, moves):
        x, y = self.x, self.y
        if not ((x-1, y-1) in old_data or
                (x, y-1) in old_data or
                (x+1, y-1) in old_data or
                (x-1, y) in old_data or
                (x+1, y) in old_data or
                (x-1, y+1) in old_data or
                (x, y+1) in old_data or
                (x+1, y+1) in old_data):
            self.move = False
            return
        self.move = True
        for m in moves:
            result = m(self, old_data, new_data)
            if result == OK:
                break
            elif result == BLOCKED:
                self.move = False
                break
        else:
            self.move = False
            new_data[self.x, self.y] = self

    def commit(self):
        if self.move:
            self.x, self.y = self.px, self.py

    def move_fail(self):
        self.move = False

    def check_move(self, suite, old_data, new_data):
        if "#" in (old_data.get(suite[0], None), old_data.get(suite[1], None), old_data.get(suite[2], None)):
            return GUARDED
        elif suite[1] in new_data:
            new_data[suite[1]].move_fail()
            self.move = False
            return BLOCKED
        else:
            new_data[suite[1]] = self
            self.px, self.py = suite[1]
            return OK

    def move_north(self, old_data, new_data):
        x, y = self.x, self.y
        suite = (x-1, y-1), (x, y-1), (x+1, y-1)
        return self.check_move(suite, old_data, new_data)

    def move_south(self, old_data, new_data):
        x, y = self.x, self.y
        suite = (x-1, y+1), (x, y+1), (x+1, y+1)
        return self.check_move(suite, old_data, new_data)

    def move_east(self, old_data, new_data):
        x, y = self.x, self.y
        suite = (x+1, y-1), (x+1, y), (x+1, y+1)
        return self.check_move(suite, old_data, new_data)

    def move_west(self, old_data, new_data):
        x, y = self.x, self.y
        suite = (x-1, y-1), (x-1, y), (x-1, y+1)
        return self.check_move(suite, old_data, new_data)

    def __repr__(self):
        return str((self.x, self.y))

def parse(f):
    data = []
    for y, line in enumerate(f):
        line = line.strip()
        for x, v in enumerate(line):
            if v == "#":
                data.append(Elf(x, y))
    return data

def solution(data, moves):
        old_data = {}
        for elf in data:
            old_data[elf.x, elf.y] = "#"

        new_data = {}
        for elf in data:
            elf.propose(old_data, new_data, moves)

        for elf in data:
            elf.commit()


def solution1(data):
    moves = [Elf.move_north, Elf.move_south, Elf.move_west, Elf.move_east]

    for _ in range(10):
        solution(data, moves)
        moves = moves[1:] + moves[:1]

        min_x, min_y, max_x, max_y = 0,0,0,0
        for elf in data:
            if elf.x < min_x:
                min_x = elf.x
            if elf.x > max_x:
                max_x = elf.x
            if elf.y < min_y:
                min_y = elf.y
            if elf.y > max_y:
                max_y = elf.y

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(data)

def solution2(data):
    moves = [Elf.move_north, Elf.move_south, Elf.move_west, Elf.move_east]
    moved = True
    ans = 0
    while moved:
        ans += 1
        moved = False
        solution(data, moves)
        moves = moves[1:] + moves[:1]
        
        for elf in data:
            if elf.move:
                moved = True
                break

    min_x, min_y, max_x, max_y = 0,0,0,0
    for elf in data:
        if elf.x < min_x:
            min_x = elf.x
        if elf.x > max_x:
            max_x = elf.x
        if elf.y < min_y:
            min_y = elf.y
        if elf.y > max_y:
            max_y = elf.y
    return ans

if __name__ == "__main__":
    with open("day23.txt") as f:
        data = parse(f)
    print(solution1(data))
    with open("day23.txt") as f:
        data = parse(f)
    print(solution2(data))

