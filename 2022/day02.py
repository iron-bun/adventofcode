#!/usr/bin/env python3

convert_move = {'X':'A','Y':'B','Z':'C'}

shape_scores = {'A':1, 'B': 2, 'C':3}
outcome_scores = {'X':0, 'Y': 3, 'Z':6}

games = {'X': {'A':'C', 'B':'A', 'C':'B'}, 'Y': {'A':'A', 'B':'B', 'C':'C'}, 'Z':{'A':'B', 'B':'C', 'C':'A'}}

def score_game(opponent, me):
    if (opponent, me) in zip(('A','B','C'),('B','C','A')):
        return 6
    elif (opponent, me) in zip(('A','B','C'),('A','B','C')):
        return 3
    else:
        return 0

def solution1(strategy): 
    ans = 0
    for line in strategy:
        line = line.strip()
        opponent, me = line.split(" ")
        me = convert_move[me]
        ans += shape_scores[me]
        ans += score_game(opponent, me)
    return ans

def solution2(strategy):
    ans = 0
    for line in strategy:
        line = line.strip()
        opponent, outcome = line.split(" ")
        ans += outcome_scores[outcome]
        ans += shape_scores[games[outcome][opponent]]
    return ans
        
with open("day2.txt") as f:
    print(solution1(f))
with open("day2.txt") as f:
    print(solution2(f))
