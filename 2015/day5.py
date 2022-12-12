#!/usr/bin/env python3

def nice_string_p1(string):

    double_char = False
    vowel_count = 0
    for chars in zip(string, string[1:]):
        if chars in (('a', 'b'), ('c', 'd'), ('p','q'), ('x','y')):
            return False

        if chars[0] == chars[1]:
            double_char = True

        if chars[0] in "aeiou":
            vowel_count += 1
    if chars[1] in "aeiou":
        vowel_count += 1

    if vowel_count < 3 or not double_char:
        return False

    return True

def nice_string_p2(string):

    split_pair = False
    repeat_group = False
    repeats = {}

    for chars in zip(string, string[2:]):
        if chars[0] == chars[1]:
            split_pair = True
            break

    for idx, chars in enumerate(zip(string, string[1:])):
        if (chars) in repeats and idx >= repeats[chars] + 2:
            repeat_group = True
            break
        elif (chars) not in repeats:
            repeats[chars] = idx

    return split_pair and repeat_group

def part1():

    puzzle_input = open("./data/day5.txt", "r")

    nice_strings = 0
    for line in puzzle_input:
        if nice_string_p1(line.strip()):
            nice_strings += 1
    return nice_strings

def part2():

    puzzle_input = open("./data/day5.txt", "r")

    nice_strings = 0
    for line in puzzle_input:
        if nice_string_p2(line.strip()):
            nice_strings += 1
    return nice_strings

if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
