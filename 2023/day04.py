#!/usr/bin/env python3

test_data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

def generate_cards(data):
  for line in data:
    line = line.strip()
    card, numbers = line.split(":")
    winners, numbers = numbers.split("|")
    card = int(card[card.rfind(" "):])
    winners = winners.split()
    numbers = numbers.split()
    win_count = len(set(winners).intersection(set(numbers)))
 
    yield card, winners, numbers, win_count

total = 0
data = open("day04.txt")
for card, winners, numbers, win_count in generate_cards(data):
  total += int(2**(win_count-1))
print(total)
data.close()

total = 0
card_dict = {}
data = open("day04.txt")
for card, winners, numbers, win_count in generate_cards(data):
  card_dict[card] = [win_count, 1]
data.close()

for i in range(1, len(card_dict)+1):
  wins, multiplier = card_dict[i]
  for j in range(1, wins+1):
    card_dict[i+j][1] += multiplier
for card in card_dict.values():
  total += card[1]
print(total)
