#!/usr/bin/env python3

import re
from queue import PriorityQueue
from itertools import permutations

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
directions = ((1,0,">"), (0,1,"v"), (-1,0,"<"), (0,-1,"^"))

layout_1_9 = {(0,0):"7", (1,0):"8", (2,0):"9",
              (0,1):"4", (1,1):"5", (2,1):"6",
              (0,2):"1", (1,2):"2", (2,2):"3",
                         (1,3):"0", (2,3):"A"}
i_layout_1_9 = {v:k for k, v in layout_1_9.items()}

layout_arrows = {           (1,0):"^", (2,0):"A",
                 (0,1):"<", (1,1):"v", (2,1):">"}
i_layout_arrows = {v:k for k, v in layout_arrows.items()}

def route(start, end, layout, i_layout):
    queue = PriorityQueue()
    queue.put((0, i_layout[start], []))
    end_space = i_layout[end]
    cost_cap = 999

    while not queue.empty():
        cost, space, path = queue.get()

        if space == end_space:
            yield path+["A"]
            if cost_cap > cost:
                cost_cap = cost
        else:
            if cost > cost_cap:
                continue

            for d in directions:
                tmp_space = tuple(map(sum, zip(space, d)))
                if layout.get(tmp_space) != None:
                    queue.put((cost+1, tmp_space, path+[d[2]]))

cache = {}
def expand(path, depth, layout, i_layout):

    length = 0
    p1 = "A"
    for c1 in path:
        if (p1, c1, depth-1) in cache:
            length += cache[p1, c1, depth-1]
        else:
            min_length = None
            for c2 in route(p1, c1, layout, i_layout):
                if depth == 0:
                    if min_length == None or len(c2) < min_length:
                        min_length = len(c2)
                else:
                    ml = expand(c2, depth-1, layout_arrows, i_layout_arrows)
                    if min_length == None or ml < min_length:
                        min_length = ml

            cache[p1, c1, depth-1] = min_length
            length += min_length
            
        p1 = c1
        
    return length

ans_1 = 0
ans_2 = 0
with open("day21.txt") as f:
    for line in f:
        length = 99
        line = line.strip()
        length_1 = expand(line, 2, layout_1_9, i_layout_1_9)
        length_2 = expand(line, 25, layout_1_9, i_layout_1_9)

        k = int("".join(re.findall("(\d)", line)))
        ans_1 += length_1 * k
        ans_2 += length_2 *k
print(ans_1)
print(ans_2)
