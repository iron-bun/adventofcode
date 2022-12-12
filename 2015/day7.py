#!/usr/bin/env python3

from lark import Lark, Transformer
import lark
wires = {}
def interp(tree):
    op = tree.data
    #print(op)
    if op == "assignment":
        wires[tree.children[1].children[0].value] = tree.children[0]
    elif op == "expression":
        return interp(tree.children[0])
    elif op == "literal":
        return int(tree.children[0].value)
    elif op == "and":
        return interp(tree.children[0]) & interp(tree.children[1])
    elif op == "value":
        return interp(tree.children[0])
    elif op == "variable":
        result = wires[tree.children[0].value]
        if type(result) == lark.tree.Tree:
            wires[tree.children[0].value] = interp(result)
        return wires[tree.children[0].value]
    elif op == "or":
        return interp(tree.children[0]) | interp(tree.children[1])
    elif op == "not":
        return ~interp(tree.children[0]) & 0xffff
    elif op == "lshift":
        return interp(tree.children[0]) << interp(tree.children[1])
    elif op == "rshift":
        return interp(tree.children[0]) >> interp(tree.children[1])
    else:
        print(f"Unknown operation: {op}")

l = Lark('''assignment: expression "->" variable
            expression: and | or | lshift | rshift | not | value
            and: value "AND" value
            or: value "OR" value
            lshift: value "LSHIFT" value
            rshift: value "RSHIFT" value
            not: "NOT" value
            value: literal | variable
            literal: NUMBER
            variable: WORD

        %import common.WORD
        %import common.INT -> NUMBER
        %ignore " "           // Disregard spaces in text
     ''', start="assignment")

def part1():

    puzzle_input = open("./data/day7.txt", "r")

    for line in puzzle_input:
        line = line.strip()
        command = l.parse(line)
        interp(command)
    return interp(wires['a'])

def part2():

    puzzle_input = open("./data/day7.txt", "r")

    for line in puzzle_input:
        line = line.strip()
        command = l.parse(line)
        interp(command)
    wires['b'] = 3176
    return interp(wires['a'])

if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
