#!/usr/bin/env python3

def parse(data):
    result = {}
    for line in data:
        if line == "\n":
            break
        node = {}
        line = line.split(" ")
        node_name = line[1]
        node['valve'] = int(line[4].split("=")[1][:-1])
        node['neighbours'] = list(map(lambda x: x[:-1], line[9:]))
        result[node_name] = node
    return result

def solution1(data):
    nodes = parse(data)
    results = {}
    max_score = 0

    queue = [("AA#", 30, 0)]
    
    while len(queue) > 0:
        queue = sorted(queue, key = lambda x: x[2], reverse=True)
        
        node, time_left, score = queue.pop(0)

        if score > max_score:
            max_score = score
        if time_left == 0:
            continue
        node_name, nodes_active = node.split("#")
        nodes_active = sorted(nodes_active.split("_"))
        
        results[node] = (time_left, score)

        prospective_score = score+(time_left-1)*nodes[node_name]['valve']
        if node_name in nodes_active:
            pass
        elif (results[node][1] < prospective_score) or (results[node][1] == prospective_score and results[node][0] < time_left):
            queue.append((f"{node_name}#{'_'.join(sorted(nodes_active + [node_name]))}", time_left-1, prospective_score))

        for n in nodes[node_name]['neighbours']:
            n = f"{n}#{'_'.join(nodes_active)}"
            if n not in results or results[n][1] < score or (results[n][1] == score and results[n][0] < time_left):
                queue.append((n, time_left-1, score))

    
    return max_score

if __name__ == "__main__":
    with open("day16.txt") as f:
        print(solution1(f))
