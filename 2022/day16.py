#!/usr/bin/env python3

def solution1(data):
    nodes = parse(data)
    results = {}
    
    queue = [("AA", 30, 0)]
    
    while len(queue) > 0:
        queue = sorted(queue, key = lambda x: x[1])
        
        node, time_left, score = queue.pop(0)
        node_name, nodes_active = node.split("#")
        nodes_active = nodes_active.split("_")
        
        if node not in nodes_active and nodes[node]['valve'] > 0:
            queue.append((f"{node}#{"_".join(sorted(nodes_active + [node]))", time_left-1, time_left*nodes[node]['value']))
        
        for n in nodes[node]['neighbours']:
            if n in results and results[n]['cost'] < 
            
    
    return 0
if __name__ == "__main__":
    with open("day_16_test.txt") as f:
        print(solution1(f))
