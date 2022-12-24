#!/usr/bin/env python3

heights = "~#abcdefghijklmnopqrstuvwxyz"
def get_height(location):
    location = location[0]
    if location == "S":
        location = "a"
    if location == "E":
        location = "z"
    return heights.find(location)

def legal_move(x1,y1,x2,y2,hills):
    default = "~"
        
    height1 = get_height(hills.get((x1,y1),(default,"#")))
    height2 = get_height(hills.get((x2,y2),(default,"#")))
    
    return height2+1 >= height1
        
def parse(data):
    hills = {}
    i,j = 0,0
    for y,row in enumerate(data):
        row = row.strip()
        for x,value in enumerate(row):
            hills[(x,y)] = (value,-1)
            if value == "E":
                i,j = x, y
    return hills, i,j
    
def solution(data):
    hills, i, j = parse(data)
    
    queue = [(i,j,0)]
    
    s_score = -1
    a_score = -1
    
    while len(queue)>0 and (s_score == -1 or a_score == -1):
        queue = sorted(queue, key=lambda x: x[2])
        
        x,y,score = queue.pop(0)
        current_height, current_score = hills[(x,y)]
        
        if current_height == "S" and s_score == -1:
            s_score = score
        
        if current_height == "a" and a_score == -1:
            a_score = score
            
        if current_score > score or current_score == -1:
            hills[(x,y)] = (current_height, score)
            
            for i,j in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]:
                if legal_move(x,y,i,j,hills):
                    queue.append((i,j, score+1))
                
    return s_score, a_score
    
if __name__ == "__main__":
    with open("day12.txt") as f:
        print(solution(f))
