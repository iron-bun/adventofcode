#!/usr/bin/env python3

letters = "abcdefghjkmnpqrstuvwxyz"

def parse_password(password):
  ans = []
  for letter in password:
    ans.append(letters.find(letter))
  return ans

def increment_password(password):
  password[-1] += 1
  if password[-1] == len(letters):
    password = increment_password(password[:-1]) + [0]
  return password

def validate_password(password):
  sequence = False
  for a, b, c in zip(password, password[1:], password[2:]):
    if a+1 == b and b+1 == c:
      sequence = True
      break

  pairs = False
  pairs_found = set()
  for idx in range(len(password)-1):
    if password[idx] == password[idx+1]:
      pairs_found.add(password[idx])
      idx += 1
    if len(pairs_found) > 1:
      pairs = True
      break
  return sequence and pairs

def encode_password(password):
  ans = ""
  for p in password:
    ans += letters[p]
  return ans

p = parse_password("hxbxwxba")
while not validate_password(p):
  p = increment_password(p)
print(encode_password(p))

p=increment_password(p)
while not validate_password(p):
  p = increment_password(p)
print(encode_password(p))
