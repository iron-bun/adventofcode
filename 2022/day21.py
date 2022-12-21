#!/usr/bin/env python3

import operator

op = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/": operator.floordiv}

def parse(monkey, monkeys):
    calc = monkeys[monkey]
    try:
        ans = int(calc)
    except:
        calc = calc.split(" ")
        ans = op[calc[1]](parse(calc[0], monkeys), parse(calc[2], monkeys))
        
    return ans
        
def solution1(data):
    monkeys = {}
    
    for line in f:
        line = line.strip()
        monkey, sum = line.split(":")
        monkeys[monkey] = sum.strip()
    return parse("root", monkeys)

def compact(monkey, monkeys):
    if monkey == "humn":
        return
        
    ans = None
    calc = monkeys[monkey]
    try:
        ans = int(calc)
    except:
        calc = calc.split(" ")
        tmp1 = compact(calc[0], monkeys)
        tmp2 = compact(calc[2], monkeys)
        if type(tmp1) == int and type(tmp2) == int:
            ans = op[calc[1]](tmp1, tmp2)
            monkeys[monkey] = ans
            del monkeys[calc[0]]
            del monkeys[calc[2]]
        elif type(tmp1) == int:
            del monkeys[calc[0]]
            monkeys[monkey] = [tmp1, calc[1], calc[2]]
        else:
            del monkeys[calc[2]]
            monkeys[monkey] = [calc[0], calc[1], tmp2]
    return ans

def solution2(data):
    monkeys = {}
    
    for line in f:
        line = line.strip()
        monkey, sum = line.split(":")
        monkeys[monkey] = sum.strip()
    monkeys["root"] = monkeys["root"].replace("+", "-")
    compact("root", monkeys)
    
    calc = monkeys["root"]
    if type(calc[0]) == int:
        ans = calc[0]
        calc = calc[2]
    else:
        ans = calc[2]
        calc = monkeys[calc[0]]
    
    while "humn" not in calc:
        if type(calc[0]) == int:
            number = calc[0]
            remainder = calc[2]
        else:
            number = calc[2]
            remainder = calc[0]
        if calc[1] == "+":
            ans -= number
        elif calc[1] == "*":
            ans //= number
        elif calc[1] == "/":
            ans *= number
        elif calc[1] == "-" and type(calc[0]) == int:
            ans = number - ans
        elif calc[1] == "-":
            ans += number
        calc = monkeys[remainder]
    
    
    return ans+calc[2]
    
if __name__ == "__main__":
    with open("day21.txt") as f:
        print(solution1(f))
    with open("day21.txt") as f:
        print(solution2(f))
