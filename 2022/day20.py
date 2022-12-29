#!/usr/bin/env python3

def solution(data):

    for i in range(len(data)):
        tmp = list((v for k, v in data if k == i))
        tmp = tmp[0]

        if tmp < 0:
            data = data[::-1]

        idx = data.index((i,tmp))
        data = data[idx:] + data[:idx]

        m = abs(tmp)
        m %= len(data)-1

        data = data[1:m+1] + [(i, tmp)] + data[m+1:]

        if tmp < 0:
            data = data[::-1]

    return data

def solution1(filename):
  with open(filename) as f:
    data = f.readlines()
    data = map(int, data)
    data = [v for v in data]
    data = list(enumerate(data))

    data = solution(data)

    data = [v for k, v in data]
    idx = data.index(0)
    data = data[idx:] + data[:idx]

    return data[1000] + data[2000] + data[3000]

def solution2(filename):
  with open(filename) as f:
    data = f.readlines()
    data = map(int, data)
    data = [v*811589153 for v in data]
    data = list(enumerate(data))

    for _ in range(10):
        data = solution(data)

    data = [v for k, v in data]
    idx = data.index(0)
    data = data[idx:] + data[:idx]

    return data[1000] + data[2000] + data[3000]

if __name__ == "__main__":
    print(solution1("day20.txt"))
    print(solution2("day20.txt"))

