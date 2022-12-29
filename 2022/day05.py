#!/usr/bin/env python3

def parse(data):
    result = {}
    commands = []
    for line in data:
        idx = 1
        if "[" in line:
            line = "".join([l for l in line[1::4]])
            for entry in line:
                if entry != " ":
                    tmp = result.get(str(idx),[])
                    tmp.append(entry)
                    result[str(idx)] = tmp
                idx += 1
        elif line == "\n":
            continue
        elif line[1] == '1':
            for key in result.keys():
                result[key]=result[key][::-1]
        else:
            tmp = line.strip().split(" ")
            commands.append((tmp[1], tmp[3], tmp[5]))
    return result, commands
        
def solution1(data):
        result, commands = parse(data)
        for count, source, dest in commands:
            for _ in range(int(count)):
                result[dest].append(result[source].pop())
        return "".join([result[k][-1] for k in sorted(result.keys())])

def solution2(data):
    result, command = parse(data)
    for count, source, dest in command:
        tmp = []
        for _ in range(int(count)):
            tmp.append(result[source].pop())
        for _ in range(int(count)):
            result[dest].append(tmp.pop())
    return "".join([result[k][-1] for k in sorted(result.keys())])

if __name__ == '__main__':
    with open("day5.txt") as f:
        print(solution1(f))
    with open("day5.txt") as f:
        print(solution2(f))
