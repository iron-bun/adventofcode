#!/usr/bin/env python3

priorities = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solution1(sacks):
    ans = 0
    for line in sacks:
        line = line.strip()
        split_point = len(line)//2

        rucksack_1, rucksack_2 = line[:split_point], line[split_point:]

        duplicate = [item for item in rucksack_1 if item in rucksack_2]
        duplicate = duplicate[0]

        ans += priorities.find(duplicate)
    return ans

def solution2(sacks):
    ans = 0
    tmp = 0
    group = []

    for line in sacks:
        line = line.strip()
        group.append(line)

        if tmp < 2:
            tmp += 1

        else:
            badge = [item for item in group[0] if item in group[1] and item in group[2]]
            badge = badge[0]

            ans += priorities.find(badge)

            tmp = 0
            group = []
    return ans

def main():
    with open("day3.txt") as f:
        print(solution1(f))
    with open("day3.txt") as f:
        print(solution2(f))

if __name__ == '__main__':
    main()
