#!/usr/bin/env python3

from lark import Lark, Transformer

grammar_part_1 = r"""
    start: start "+" value -> add
         | start "*" value -> mul
         | value

    value: SIGNED_NUMBER -> number
         | sub_statement

    sub_statement: "(" start ")"

    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

"""

grammar_part_2 = r"""
    start: mul

    ?mul: add
       | mul "*" mul

    add: value
       | add "+" add

    value: NUMBER -> number
         | sub_statement

    sub_statement: "(" mul ")"

    %import common.NUMBER
    %import common.WS
    %ignore WS

"""

class statement_transformer(Transformer):
    def start(self, items):
        return items[0]
    def number(self, items):
        return int(items[0])
    def add(self, items):
        return sum(items)
    def mul(self, items):
        return items[0] * items[1]
    def sub_statement(self, items):
        return items[0]
    def value(self, items):
        return items[0]
        

def solution(f, grammar):

    ans = 0
    parser = Lark(grammar, parser="lalr", transformer=statement_transformer())
    evaluate = parser.parse

    for line in f:
        tmp = evaluate(line)
        ans += tmp

    return ans

if __name__ == "__main__":
    with open("day18.txt") as f:
        print(solution(f, grammar_part_1))
    with open("day18.txt") as f:
        print(solution(f, grammar_part_2))
