#!/usr/bin/env python3

class Wall:
    def __init__(self, location):
        self.location = location
    def check_move(self, direction, layout):
        return False
    def move(self, direction, layout):
        return False
    def print(self, location):
        print("#", end="")
    def calc_move(self, location, direction):
        return tuple(map(sum, zip(location, direction)))

class Box(Wall):
    def move(self, direction, layout):
        new_location = tuple(map(sum,zip(self.location, direction)))
        neighbour = layout.get(new_location)
        if neighbour == None or neighbour.move(direction, layout):
            layout[self.location] = None
            self.location = new_location
            layout[self.location] = self
            return True
        else:
            return False
    def print(self, location):
        print("O", end="")

class Robot(Box):
    def print(self, location):
        print("@", end="")

directions = {"<":(-1, 0), "v": (0, 1), ">": (1, 0), "^": (0, -1)}

layout = {}
with open("day15.txt") as f:
    for y, line in enumerate(f):
        line = line.strip()
        if line == "":
            break
        for x, char in enumerate(line):
            item = None
            if char == "#":
                item = Wall((x, y))
            elif char == "O":
                item = Box((x, y))
            elif char == "@":
                item = Robot((x, y))
                robot = item
            layout[x,y] = item
    for line in f:
        line = line.strip()
        for char in line:
            robot.move(directions[char],layout)
ans = 0
for k in layout:
    if layout[k] == None or type(layout[k]) is Robot:
        continue
    if type(layout[k]) is Box:
        ans += k[0]+k[1]*100
print(ans)

class BigBox(Box):
    def check_neighbour(self, location, direction, layout):
        neighbour = layout.get(location)
        if neighbour == None:
            return True
        elif neighbour.check_move(direction, layout):
            return True
        else:
            return False
        
    def check_move(self, direction, layout):
                
        new_location = self.calc_move(self.location, direction)
        if direction == (1,0):
            new_location = self.calc_move(new_location, direction)
        
        if not self.check_neighbour(new_location, direction, layout):
            return False

        if (direction == (0,1) or direction == (0,-1)) and not self.check_neighbour(self.calc_move(new_location, (1,0)), direction, layout):
            return False

        return True
        
    def move(self, direction, layout):
        if not self.check_move(direction, layout):
            return False
        
        new_location = self.calc_move(self.location, direction)
        if direction == (1,0):
            new_location = self.calc_move(new_location, direction)

        neighbours = set()
        neighbours.add(layout.get(new_location))
        if direction in ((0,1), (0,-1)):
            neighbours.add(layout.get(self.calc_move(new_location, (1,0))))
        
        for neighbour in neighbours:
            if neighbour == None or neighbour == self:
                continue
            neighbour.move(direction, layout)
            
        layout[self.location] = None
        layout[self.calc_move(self.location, (1,0))] = None

        self.location = self.calc_move(self.location, direction)
        layout[self.location] = self
        layout[self.calc_move(self.location, (1,0))] = self

        return True

    def print(self, location):
        if location == self.location:
            print("[]", end="")

layout = {}
with open("day15.txt") as f:
    for y, line in enumerate(f):
        line = line.strip()
        if line == "":
            break
        for x, char in enumerate(line):
            x *= 2
            item = None
            if char == "#":
                item = Wall((x, y))
                layout[x,y] = item
                item = Wall((x+1, y))
                layout[x+1,y] = item
            elif char == "O":
                item = BigBox((x, y))
                layout[x,y] = item
                layout[x+1,y] = item
            elif char == "@":
                item = Robot((x, y))
                layout[x,y] = item
                robot = item

    for line in f:
        line = line.strip()
        for char in line:
            robot.move(directions[char],layout)
            
ans = 0
for k in layout:
    if layout[k] == None or type(layout[k]) is Robot:
        continue
    if type(layout[k]) is BigBox and k == layout[k].location:
        ans += k[0]+k[1]*100
print(ans)
