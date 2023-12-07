#!/usr/bin/env python3

test_data = ["32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483"]

card_ranks = {k:v+2 for v, k in enumerate(list('AKQJT98765432')[::-1])}

result_lookup = {k:v for v, k in enumerate([(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (3,2), (4, 1), (5,)])}

def get_hand_type(hand, wildcard=False):
  hand = sorted(hand)
  result = []
  tmp_card = ""
  tmp_count = 0
  joker_count = 0

  for card in hand:
    if card == "J":
      joker_count += 1
    elif card != tmp_card:
      result.append(tmp_count)
      tmp_card = card
      tmp_count = 1
    else:
      tmp_count += 1
  result.append(tmp_count)

  if not wildcard:
    result.append(joker_count)
    result = sorted(result, reverse=True)
  elif len(result) > 0:
    result = sorted(result, reverse=True)
    result[0] += joker_count
  else:
    result = [5]
  
  while 0 in result:
    result.remove(0)

  return result_lookup[tuple(result)]

def parse_cards(cards, ranks=card_ranks, wildcard=False):
  result = []
  for card in cards:
    card = card.strip()

    hand, bid = card.split(" ")
    hand = [get_hand_type(hand, wildcard)] + [ranks[k] for k in hand]

    bid = int(bid)
    result.append((hand, bid))
  return result

with open("day07.txt") as data:
  hands = parse_cards(data)
hands = sorted(hands, key=lambda x:x[0])
ans = 0
for hand in enumerate(hands):
  ans += (hand[0]+1) * hand[1][1]
print(ans)

joker_card_ranks = {k:v+1 for v, k in enumerate(list('AKQT98765432J')[::-1])}
with open("day07.txt") as data:
  hands = parse_cards(data, joker_card_ranks, True)
hands = sorted(hands, key=lambda x:x[0])
ans = 0
for hand in enumerate(hands):
  ans += (hand[0]+1) * hand[1][1]
print(ans)
