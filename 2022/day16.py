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
    working_valves = "_" + "_".join(sorted([k for k in nodes.keys() if nodes[k]['valve'] > 0]))
    print(working_valves)
    queue = [("AA#", 30, 0)]
    
    while len(queue) > 0:
        queue = sorted(queue, key = lambda x: x[2], reverse=True)
        
        node, time_left, score = queue.pop(0)

        if score > max_score:
            max_score = score
        if time_left == 0:
            continue
        node_name, nodes_active = node.split("#")
        if nodes_active == working_valves:
            continue
        nodes_active = sorted(nodes_active.split("_"))
        
        results[node] = (time_left, score)

        prospective_score = score+(time_left-1)*nodes[node_name]['valve']
        if node_name in nodes_active or nodes[node_name]['valve']==0:
            pass
        #elif (results[node][1] < prospective_score) or (results[node][1] == prospective_score and results[node][0] < time_left):
        else: #if (results[node][1] < prospective_score) or (results[node][1] == prospective_score and results[node][0] < time_left):
            queue.append((f"{node_name}#{'_'.join(sorted(nodes_active + [node_name]))}", time_left-1, prospective_score))

        for n in nodes[node_name]['neighbours']:
            n = f"{n}#{'_'.join(nodes_active)}"
            if n not in results or results[n][1] < score or (results[n][1] == score and results[n][0] < time_left-1):
                queue.append((n, time_left-1, score))

    
    return max_score

def solution2(data):
    nodes = parse(data)
    results = {}
    max_score = 0
    working_valves = "_" + "_".join(sorted([k for k in nodes.keys() if nodes[k]['valve'] > 0]))
    print(working_valves)

    queue = [("AA_AA#", 26, 0)]

    while len(queue) > 0:
        queue = sorted(queue, key = lambda x: x[2], reverse=True)
        #print(max_score, max_score, queue)

        node, time_left, score = queue.pop(0)
        #print(max_score, len(queue), node, time_left, score)

        if score > max_score:
            max_score = score
            print(max_score)

        if time_left == 0:
            continue

        node_names, nodes_active = node.split("#")
        if nodes_active == working_valves:
            continue

        np, ne = node_names.split("_")
        del node_names

        nodes_active = sorted(nodes_active.split("_"))

        results[node] = (time_left, score)
        #print(results)

        #try a double activation
        if np == ne:
            pass
        elif np in nodes_active or nodes[np]['valve'] == 0:
            pass
        elif ne in nodes_active or nodes[ne]['valve'] == 0:
            pass
        else: 
            prospective_score = score + (time_left-1)*nodes[np]['valve'] + (time_left-1)*nodes[ne]['valve']
            queue.append((f"{np}_{ne}#{'_'.join(sorted(nodes_active + [np, ne]))}", time_left-1, prospective_score))
            print(max_score, len(queue), "activating", np, ne)
        if nodes[ne]['valve'] == 0:
            np, ne = ne, np

        #definitely move the person
        for np in nodes[np]['neighbours']:

            #move person activate elephant
            if ne in nodes_active or nodes[ne]['valve'] == 0:
                pass
            else: 
                prospective_score = score + (time_left-1)*nodes[ne]['valve']
                new_nodes = f"{'_'.join(sorted((np, ne)))}"
                queue.append((f"{new_nodes}#{'_'.join(sorted(nodes_active + [ne]))}", time_left-1, prospective_score))
                #print(max_score, len(queue), "appending", np, "activating", ne)

            #double move
            for ne1 in nodes[ne]['neighbours']:
                new_nodes = f"{'_'.join(sorted((np, ne1)))}#{'_'.join(nodes_active)}"
                if new_nodes not in results or results[new_nodes][1] < score or (results[new_nodes][1] == score and results[new_nodes][0] < time_left-1):
                    queue.append((new_nodes, time_left-1, score))
                    #print(max_score, len(queue), "appending", np, ne1)


    return max_score
if __name__ == "__main__":
    with open("day16.txt") as f:
        print(solution1(f))
    with open("day16.txt") as f:
        print(solution2(f))

