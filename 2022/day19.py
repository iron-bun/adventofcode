#!/usr/bin/env python3

class Blueprint:
    def __init__(self, costs):
        self.orebot_cost, self.claybot_cost, self.obsbot_cost, self.geodebot_cost = costs
        self.orebots, self.claybots, self.obsbots, self.geodebots = 1,0,0,0

    def process(self, resources):
        time, ore, clay, obsidian, geodes, orebots, claybots, obsbots, geodebots = resources

        time += 1

        yield (time, ore+orebots, clay+claybots, obsidian+obsbots, geodes+geodebots, orebots, claybots, obsbots, geodebots)

        while True:

            c_ore, c_clay, c_obs = ore, clay, obsidian
            c_bots = claybots
            while True:

                o_ore, o_clay, o_obs = c_ore, c_clay, c_obs
                o_bots = obsbots
                while True:

                    g_ore, g_clay, g_obs = o_ore, o_clay, o_obs
                    g_bots = geodebots
                    while True:

                        if Blueprint.can_afford((g_ore, g_clay, g_obs), self.geodebot_cost):
                            g_ore, g_clay, g_obs = Blueprint.purchase((g_ore, g_clay, g_obs), self.geodebot_cost)
                            yield (time, g_ore+orebots, g_clay+c_bots, g_obs+o_bots, geodes+g_bots, orebots, c_bots, o_bots, g_bots+1)
                            g_bots += 1
                        else:
                            break

                    if Blueprint.can_afford((o_ore, o_clay, o_obs), self.obsbot_cost):
                        o_ore, o_clay, o_ob = Blueprint.purchase((o_ore, o_clay, o_obs), self.obsbot_cost)
                        yield (time, o_ore+orebots, o_clay+c_bots, o_obs+o_bots, geodes+geodebots, orebots, c_bots, o_bots+1, geodebots)
                        o_bots += 1
                    else:
                        break

                if Blueprint.can_afford((c_ore, c_clay, c_obs), self.claybot_cost):
                    c_ore, c_clay, c_obs = Blueprint.purchase((c_ore, c_clay, c_obs), self.claybot_cost)
                    yield (time, c_ore+orebots, c_clay+c_bots, c_obs+obsbots, geodes+geodebots, orebots, c_bots+1, obsbots, geodebots)
                    c_bots += 1
                else:
                    break

            if Blueprint.can_afford((ore, clay, obsidian), self.orebot_cost):
                ore, clay, obsidian = Blueprint.purchase((ore, clay, obsidian), self.orebot_cost)
                yield (time, ore+orebots, clay+claybots, obsidian+obsbots, geodes+geodebots, orebots+1, claybots, obsbots, geodebots)
                orebots += 1
            else:
                break

    def can_afford(resources, cost):
        for i, j in zip(resources, cost):
            if j > i:
                return False
        else:
            return True
    def purchase(resources, cost):
        ans = []
        for i, j in zip(resources, cost):
            ans.append(i-j)
        return ans

def score(outcome, bp):
    t,r,c,o,g,rb,cb,ob,gb = outcome
    score = 0
    if cb == 0:
        score += (bp.claybot_cost[0] - r) / rb
    elif ob == 0:
        score += (bp.obsbot_cost[1] - c) / cb
    else:
        score += (bp.geodebot_cost[2] - o) / ob
    score = max(score, 0)
    print(outcome, score)
    return score
    return r + c + o + g + 1*rb + 2*cb + 3*ob + 4*gb

def solution1(data):
    bp = data.split(" ")
    bp_id = int(bp[1][-2])
    rb_cost = (int(bp[6]), 0, 0)
    cb_cost = (int(bp[12]), 0, 0)
    ob_cost = (int(bp[18]), int(bp[21]), 0)
    gb_cost = (int(bp[27]), 0, int(bp[30]))
    b = Blueprint((rb_cost, cb_cost, ob_cost, gb_cost))
    r = (0,0,0,0,0,1,0,0,0)

    queue = set()
    queue.add(r)
    ans = 0
    resolved = set()
    score_per_minute = {v:None for v in range(25)}

    while len(queue) > 0:
        queue = sorted(queue, key=lambda x: x[8]*1000 + x[7]*100 + x[6]*10 +x[5], reverse=False)
        tmp = queue.pop()
        if tmp in resolved:
            continue

        if score_per_minute[tmp[0]] == None:
            score_per_minute[tmp[0]] = score(tmp, b) 
        elif score(tmp, b) >= score_per_minute[tmp[0]]:
            continue
        else:
            score_per_minute[tmp[0]] = score(tmp, b)

        resolved.add(tmp)

        if tmp[4] > ans:
            ans = tmp[4]
            print("*", ans)
        if tmp[0] >= 24:
            continue
        for outcome in b.process(tmp):
            #if score(tmp,b) > score_per_minute[tmp[0]]:
                queue.append(outcome)
                #print(tmp, outcome)
        
    return ans*bp_id

if __name__ == '__main__':
    ans = 0
    with open("day19.txt") as f:
        for line in f:
            line = line.strip()
            ans += solution1(line)
            print(ans)
    print("***")
    print(ans)

#172 is too low
