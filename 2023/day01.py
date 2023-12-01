#!/usr/bin/env python3

total = 0
with open("day01.txt") as data:
  for line in data:
    digits = [d for d in line if d.isnumeric()]
    value = digits[0] + digits[-1]
    total += int(value)
print(total)

names = {
  "1":"1",
  "2":"2",
  "3":"3",
  "4":"4",
  "5":"5",
  "6":"6",
  "7":"7",
  "8":"8",
  "9":"9",
  "two":"2", 
  "one":"1", 
  "three":"3", 
  "four":"4", 
  "five":"5", 
  "six":"6", 
  "seven":"7", 
  "nine":"9",
  "eight":"8"
}

def find_digit(value, search_backwards=False):
  if search_backwards:
    f = str.rfind
  else:
    f = str.find

  positions = {f(value, k):k for k in names.keys() if f(value,k) != -1}
    
  if search_backwards:
    tmp = sorted(positions.keys())[-1]
  else:
    tmp = sorted(positions.keys())[0]

  return names[positions[tmp]]

total = 0
with open("day01.txt") as data:
  for line in data:
    line = line.strip()
    line = [find_digit(line), find_digit(line, True)]
    total += int(line[0] + line[-1])
print(total)
