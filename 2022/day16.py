#!/usr/bin/env python3

from queue import PriorityQueue

def parse(data):
    result = {}
    for line in data:
        if line == "\n":
            break
        node = {}
        line = line.split(" ")
        node_name = line[1]
        node['valve'] = int(line[4].split("=")[1][:-1])
        node['neighbours'] = [(n[:-1], 1) for n in line[9:]]
        result[node_name] = node

    return result

def compact_map(data):
    new_map = {}
    for n in data:
        if data[n]['valve'] == 0 and n != 'AA':
            continue
        queue = PriorityQueue()
        queue.put((0, n))
        neighbours = []
        resolved = []
        new_map[n] = {}

        while not queue.empty():
            node_cost, node = queue.get()

            if data[node]['valve'] > 0 and node_cost > 0 and (node, node_cost) not in neighbours:
                neighbours.append((node, node_cost))

            resolved.append(node)

            for neighbour, neighbour_cost in data[node]['neighbours']:
                if neighbour in resolved:
                    continue
                queue.put((node_cost + neighbour_cost, neighbour))

        new_map[n]['neighbours'] = neighbours
        new_map[n]['valve'] = data[n]['valve']

    return new_map


QUEUE_ORDER = -1

def solution1(data):
    nodes = parse(data)
    nodes = compact_map(nodes)

    results = {}
    max_score = 0

    queue = PriorityQueue()
    queue.put((0, "AA#", 30, None))

    while not queue.empty():
        
        score, node, time_left, prev_node = queue.get_nowait()
        score *= QUEUE_ORDER

        if score > max_score:
            max_score = score
        if time_left <= 0:
            continue

        node_name, all_nodes_active = node.split("#")

        nodes_active = all_nodes_active.split("_")
        
        results[node] = (time_left, score)

        if node_name in nodes_active or nodes[node_name]['valve']==0:
            for n, n_cost in nodes[node_name]['neighbours']:
                if time_left - n_cost < 1 or n in nodes_active:
                    continue
                n = f"{n}#{all_nodes_active}"
                if n not in results or results[n][1] < score or (results[n][1] == score and results[n][0] < time_left - n_cost):
                    queue.put_nowait((score*QUEUE_ORDER, n, time_left - n_cost, node_name))
        else: 
            prospective_score = score+(time_left-1)*nodes[node_name]['valve']
            queue.put_nowait((prospective_score * QUEUE_ORDER, f"{node_name}#{'_'.join(sorted(nodes_active + [node_name]))}", time_left - 1, None))

    return max_score

def solution2(data):
    nodes = parse(data)
    nodes = compact_map(nodes)

    results = {}
    max_score = 0

    queue = PriorityQueue()
    queue.put((0, 0, "AA", 0, "AA", ""))

    while not queue.empty():
       score, time_used, ne, time_used_2, np, all_nodes_active = queue.get()
       score *= QUEUE_ORDER

       if score > max_score:
           max_score = score

       results[f"{'_'.join(sorted([np, ne]))}#{all_nodes_active}"] = (score, time_used, time_used_2)

       for n in nodes[ne]['neighbours']:
           if n[0] in all_nodes_active:
               continue

           new_time = time_used + n[1] + 1
           if new_time >= 26:
               continue

           new_score = QUEUE_ORDER * (score + (nodes[n[0]]['valve'] * (26-new_time))) 
           new_active = "_".join(sorted(all_nodes_active.split("_") + [n[0]]))
           new_results_key = f"{'_'.join(sorted([np, n[0]]))}#{new_active}"

           if new_time >= time_used_2:
               low_time, high_time = time_used_2, new_time
               low_move, high_move = np, n[0]
           else:
               low_time, high_time = new_time, time_used_2
               low_move, high_move = n[0], np

           if new_results_key not in results:
               pass
           elif results[new_results_key][1] < low_time or results[new_results_key][2] < high_time:
               continue

           prepare_values = (new_score, low_time, low_move, high_time, high_move, new_active)
           queue.put(prepare_values)

    return max_score

if __name__ == "__main__":
    with open("day16.txt") as f:
        print(solution1(f))
    with open("day16.txt") as f:
        print(solution2(f))

