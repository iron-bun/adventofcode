#!/usr/bin/env python3

from math import ceil

def get_neighbours(state, bp):
    t, rb, cb, ob, gb, r, c, o, g = state
    max_r_cost = max([bp[idx][0] for idx in range(4)])
    max_c_cost = max([bp[idx][1] for idx in range(4)])
    max_o_cost = max([bp[idx][2] for idx in range(4)])
    
    if gb > 0 and t < 24:
        yield 24, rb, cb, ob, gb, r+rb*(24-t), c+cb*(24-t), o+ob*(24-t), g+gb*(24-t)

    if ob > 0:
        new_time = 1 + max(ceil((bp[3][0]-r) / rb), ceil((bp[3][2]-o) / ob), 0)
        yield t+new_time, rb, cb, ob, gb+1, r+rb*new_time-bp[3][0], c+cb*new_time, o+ob*new_time-bp[3][2], g+gb*new_time

    if cb > 0 and ob <= max_o_cost:
        new_time = 1 + max(ceil((bp[2][0]-r) / rb), ceil((bp[2][1]-c) / cb), 0)
        yield t+new_time, rb, cb, ob+1, gb, r+rb*new_time-bp[2][0], c+cb*new_time-bp[2][1], o+ob*new_time, g+gb*new_time

    if cb <= max_c_cost:
        new_time = 1 + max(ceil((bp[1][0]-r) / rb), 0)
        yield t+new_time, rb, cb+1, ob, gb, r+rb*new_time-bp[1][0], c+cb*new_time, o+ob*new_time, g+gb*new_time

    if rb <= max_r_cost:
        new_time = 1 + max(ceil((bp[0][0]-r) / rb), 0)
        yield t+new_time, rb+1, cb, ob, gb, r+rb*new_time-bp[0][0], c+cb*new_time, o+ob*new_time, g+gb*new_time

def parse(line):
    bp = line.split(" ")
    bp_id = int(bp[1][-2])
    rb_cost = (int(bp[6]), 0, 0)
    cb_cost = (int(bp[12]), 0, 0)
    ob_cost = (int(bp[18]), int(bp[21]), 0)
    gb_cost = (int(bp[27]), 0, int(bp[30]))

    return (rb_cost, cb_cost, ob_cost, gb_cost)

def solution1(f):
    ans = 0

    for idx, line in enumerate(f):
        idx += 1
        #if idx != 12:
            #continue
        bp = parse(line)
        print(idx)
        for v in bp:
            print(v)
        state = (0,1,0,0,0,0,0,0,0)

        #for n in get_neighbours((12, 1, 4, 1, 0, 1, 7, 1, 0), bp):
            #print(n)
        #exit()

        queue = [state]
        resolved = set()

        tmp = 0
        while len(queue) > 0:
            state = queue.pop(0)

            if state in resolved:
                #print("resolved hit")
                continue
            #print(state)
            resolved.add(state)

            if state[0] > 24:
                continue
            #print(state)

            if state[-1] > tmp:
                tmp = state[-1]

            for n in get_neighbours(state, bp):
                if n[0] <= 24:
                    queue.append(n)

        ans += tmp * (idx)
        print("***", tmp)
    return ans

if __name__ == "__main__":
    with open("day19.txt") as f:
        print(solution1(f))
#524 too low
