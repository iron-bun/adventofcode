#!/usr/bin/env python3

def parse_data(data):
    max_depth = 0
    caves = {}
    for line in data:
        line = line.strip()
        line = line.split(" -> ")
        line = list(map(lambda x: x.split(","), line))
        line = [list(map(int, v)) for v in line]
        
        for start, stroke in zip(line, line[1:]):
            #print(start, stroke)
            if start[0] == stroke[0]:
                start, stop = min(start[1], stroke[1]), max(start[1], stroke[1])
                for i in range(start, stop+1):
                    caves[stroke[0], i] = "#"
                    if i > max_depth:
                        max_depth = i
                        
            elif start[1] == stroke[1]:
                start, stop = min(start[0], stroke[0]), max(start[0], stroke[0])
                for i in range(start, stop+1):
                    caves[i, stroke[1]] = "#"
                    if stroke[1] > max_depth:
                        max_depth = stroke[1]
                    
            else:
                print("diagonal line?", start, stroke)
                exit(1)
                
    return caves, max_depth
    
def solution1(data):
    caves, max_depth = parse_data(data)
    
    sand_falling = True
    ans = 0
    
    
    while sand_falling:
    
        grain = (500,0)
        
        while grain not in caves and grain[1] < max_depth+10:
            
            x, y = grain
            if y > max_depth:
                sand_falling = False
                break
                
            elif (x, y+1) not in caves:
                y += 1
                
            elif (x-1, y+1) not in caves:
                x -= 1
                y += 1
            
            elif (x+1, y+1) not in caves:
                x+=1
                y+=1
                
            else:
                caves[(x, y)] = "o"
                ans += 1
                grain = (500,0)
                
            grain = x, y
    return ans
            
        
def solution2(data):
    caves, max_depth = parse_data(data)
    max_depth += 2
    
    sand_falling = True
    ans = 0
    
    falling_chain = [(500, 0)]
    
    while sand_falling:

        x, y = falling_chain.pop()

        while (x, y) not in caves and y < max_depth+10:
            
            if y+1 == max_depth:
                caves[(x, y)] = "o"
                ans += 1

            elif (x, y+1) not in caves:
                falling_chain.append((x, y))
                y += 1
                
            elif (x-1, y+1) not in caves:
                falling_chain.append((x, y))
                x -= 1
                y += 1
            
            elif (x+1, y+1) not in caves:
                falling_chain.append((x, y))
                x+=1
                y+=1
                
            else:
                caves[(x, y)] = "o"
                ans += 1
                
                if (x, y) == (500, 0):
                    sand_falling = False
                    break
            
    return ans
    
if __name__ == "__main__":
    with open("day14.txt") as f:
        print(solution1(f))
    with open("day14.txt") as f:
        print(solution2(f))
