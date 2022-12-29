#!/usr/bin/env python3

class tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = False
        self.north, self.east, self.south, self.west = None, None, None, None

    def add_north(self, other):
        self.north = other
        other.add_south(self)
    def add_west(self, other):
        self.west = other
        other.add_east(self)
    def add_south(self, other):
        self.south = other
    def add_east(self, other):
        self.east = other
        
    def check_visible(self):
        if self.look("north") < self.height or self.look("east") < self.height or self.look("south") < self.height or self.look("west") < self.height:
            self.visible = True
            
    def check_viewing_distance(self):
        self.viewing_distance = self.view("north") * self.view("east") * self.view("south") * self.view("west")
        
    def view(self, direction):
        ans = 0
        tmp = getattr(self, direction)
        if tmp == None:
            return ans
        
        max_height = tmp.height
        while tmp != None:
            ans += 1
            if tmp.height >= self.height:
                break
            tmp = getattr(tmp, direction)
        return ans
        
    def look(self, direction):
        tmp = getattr(self, direction)
        if tmp == None:
            return -1
        
        ans = 0
        while tmp != None:
            if tmp.height > ans:
                ans = tmp.height
            tmp = getattr(tmp, direction)
        return ans
    
class forest:
    def __init__(self, data):
        self.trees = []
        for i, row in enumerate(data):
            self.trees.append([])
            for j, height in enumerate(row.strip()):
                t = tree(height)
                if i > 0:
                    t.add_north(self.trees[i-1][j])
                if j > 0:
                    t.add_west(self.trees[i][j-1])
                self.trees[i].append(t)
                

    
def solution1(data):
    f = forest(data)
    ans = 0
    for row in f.trees:
        for t in row:
           t.check_visible()
           if t.visible:
               ans += 1
    return ans
    
def solution2(data):
    f = forest(data)
    ans = 0
    for row in f.trees:
        for t in row:
            t.check_viewing_distance()
            if t.viewing_distance > ans:
                ans = t.viewing_distance
    return ans
    
    
if __name__ == "__main__":
    with open("day8.txt") as f:
        print(solution1(f.readlines()))
    with open("day8.txt") as f:
        print(solution2(f.readlines()))
