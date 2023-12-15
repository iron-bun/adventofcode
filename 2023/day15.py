#!/usr/bin/env python3

def hash_word(word):
    ans = 0
    for char in word:
        ans += ord(char)
        ans *= 17
        ans %= 256
    return ans

ans = 0
with open("day15.txt") as f:
    line = f.read().strip().split(",")
    for word in line:
        ans += hash_word(word)
print(ans)

lens_boxes = [[] for _ in range(256)]
final_power = {}

with open("day15.txt") as f:
    line = f.read().strip().split(",")
    for word in line:
        if "=" in word:
            label, power = word.split("=")
            box = lens_boxes[hash_word(label)]
            if label not in box:
              box.append(label)
            final_power[label] = int(power)
        else:
            label = word[:-1]
            box = lens_boxes[hash_word(label)]
            if label in box:
                del box[box.index(label)]
    for label, power in final_power.items():
        box = lens_boxes[hash_word(label)]
        if label in box:
          box[box.index(label)] = power

    ans = 0
    for i, box in enumerate(lens_boxes):
        for j, lens in enumerate(box):
            ans += (i+1) * (j+1) * lens
    print(ans)

