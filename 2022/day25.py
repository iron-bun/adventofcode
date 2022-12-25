#!/usr/bin/env python3

glyphs = {"=":-2, "-":-1, "0":0, "1":1, "2":2}

def decode(snafu):
    snafu = snafu.strip()
    ans = 0
    exp = 0
    digits = list(snafu)
    for d in digits[::-1]:
        d = glyphs[d]
        ans += 5**exp * d
        exp += 1
    return ans

def encode(value):
    snafu = ""
    carry = 0
    while value > 1:
        tmp = value // 5
        remainder = value%5
        remainder += carry
        carry = 0
        if remainder == 5:
            carry = 1
            snafu = "0" + snafu
        elif remainder == 4:
            carry = 1
            snafu = "-" + snafu
        elif remainder == 3:
            carry = 1
            snafu = "=" + snafu
        else:
            snafu = str(remainder) + snafu
        value = tmp
    snafu = str(remainder-1) + snafu
    return snafu

with open("day25.txt") as f:
    ans = sum([decode(v) for v in f])
    ans = encode(ans)
    print(ans)
