#!/usr/bin/env python3

def part1():
    puzzle_input = [
        r"aaa\"aaa"
    ]

    puzzle_input = open("./data/day8.txt", "r").readlines()

    total_chars = 0
    escaped_chars = 0
    for line in puzzle_input:
        line = line.strip()
        total_chars += len(line)

        chars = []
        idx = 0
        while idx < len(line):
            if line[idx] == "\"":
                idx += 1
            elif line[idx] != "\\":
                chars.append(line[idx])
                idx += 1
            elif line[idx+1] == "x":
                chars.append(chr(int(f"0x{line[idx+2:idx+4]}", 16)))
                idx += 4
            else:
                chars.append(line[idx+1])
                idx += 2
        escaped_chars += len(chars)

    return total_chars - escaped_chars

def part2():
    puzzle_input = [
    "\"\"",
    "\"abc\"",
    "\"aaa\\\"aaa\"",
    "\"\x27\""
    ]
    puzzle_input = open("./data/day8.txt", "r").readlines()

    total_chars = 0
    escaped_chars = 0
    for line in puzzle_input:
        line = line.strip()
        total_chars += len(line)

        chars = ["\""]
        idx = 0
        for char in line:
            if char == "\"":
                chars.append("\\")
                chars.append("\"")
            elif char == "\\":
                chars.append("\\")
                chars.append("\\")
            else:
                chars.append(char)
        chars.append("\"")
        escaped_chars += len(chars)
    return escaped_chars - total_chars


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
