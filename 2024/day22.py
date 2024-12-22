#!/usr/bin/env python3

results = {}

def randomise(ans):
    ans ^= ans << 6
    ans &= 16777215
    ans ^= ans >> 5
    ans ^= ans << 11
    ans &= 16777215

    return ans

with open("day22.txt") as f:
    ans = 0
    for line in f:
        history = []
        line = int(line)
        prev = line%10
        line_history = []
        for _ in range(2000):
            line = randomise(line)            
            tmp = line%10
            
            history.append(tmp-prev)
            tmp_history = tuple(history)
            
            if len(tmp_history) == 4:
                if tmp_history not in line_history:
                    results[tmp_history] = results.get(tmp_history, 0) + tmp
                    line_history.append(tmp_history)
                history.pop(0)
            prev = tmp
        ans += line

print(ans)
print(max(results.values()))
