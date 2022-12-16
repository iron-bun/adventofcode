#!/usr/bin/env python3


def parse_line(data):
    sensor = []
    beacon = []
    
    data = data.split(" ")
    
    sensor.append(int(data[2][:-1].split("=")[1]))
    sensor.append(int(data[3][:-1].split("=")[1]))
    
    beacon.append(int(data[8][:-1].split("=")[1]))
    beacon.append(int(data[9][:-1].split("=")[1]))
    
    return sensor, beacon

def manhatten_distance(sensor, beacon):
    return sum([abs(x-y) for x, y in zip(sensor, beacon)])

def merge_ranges(ranges):
    ans = []
    tmp = ranges.pop()
    merged = True
    while len(ranges) > 0:
        if not merged:
            ans.append(tmp)
            tmp = ranges.pop()
        merged = False
        
        for r in ranges[:]:
            
            if tmp[0] >= r[0] and tmp[1] <= r[1]:
                tmp = r
                del ranges[ranges.index(r)]
                merged = True
                break
            elif tmp[0] <= r[0] and tmp[1] >= r[1]:
                del ranges[ranges.index(r)]
                merged = True
                break
            elif tmp[0] < r[0] and r[0] <= tmp[1]+1 <= r[1]:
               tmp = (tmp[0], r[1])
               del ranges[ranges.index(r)]
               merged = True
               break
            elif r[0] <= tmp[0]-1 <= r[1] and tmp[1] > r[1]:
               tmp = (r[0], tmp[1])
               del ranges[ranges.index(r)]
               merged = True
               break
    ans.append(tmp)
               
    return ans
    
def solution1(data, row):
    
    ranges = []
    gear = []
    for line in data:
        sensor, beacon = parse_line(line)
        distance = manhatten_distance(sensor, beacon)
        if abs(row - sensor[1]) > distance:
            continue
        
        r = distance - abs(sensor[1] - row)
        ranges.append((sensor[0] - r, sensor[0] + r))
        gear.append(sensor)
        gear.append(beacon)
    
    ranges = merge_ranges(ranges)
    
    r = ranges[0]
    
    return r[1]-r[0]

def solution2(data, size):
    
    ranges = []
    gear = []
    for line in data:
        sensor, beacon = parse_line(line)
        distance = manhatten_distance(sensor, beacon)
        
        gear.append([sensor,distance])
    
    for idx in range(size):
        
        ranges = []
        tmp = [(s,d-abs(idx-s[1])) for s, d in gear if abs(idx-s[1]) < d]
        
        for t in tmp:
            ranges.append([t[0][0]-t[1], t[0][0]+t[1]])
        ranges = merge_ranges(ranges)
        
        if len(ranges) > 1:
            ranges = sorted(ranges, key=lambda x: x[0])
            return ((ranges[0][1]+1) * 4000000) + idx
    
def scan(gear, start, end):
    for idx in range(start, end+1):
        #print(idx)
        ranges = []
        tmp = [(s,d-abs(idx-s[1])) for s, d in gear if abs(idx-s[1]) < d]
        
        for t in tmp:
            ranges.append([t[0][0]-t[1], t[0][0]+t[1]])
        ranges = merge_ranges(ranges)
        
        if len(ranges) > 1:
            ranges = sorted(ranges, key=lambda x: x[0])
            return ((ranges[0][1]+1) * 4000000) + idx
            
if __name__ == "__main__":
    with open("day15.txt") as f:
        print(solution1(f,2000000))
    with open("day15.txt") as f:
        print(solution2(f,4000000))
