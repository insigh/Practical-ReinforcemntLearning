"""
5 4
1 2 2 10 1
1 3
2 2 5
2 4 3
1 4
"""
# coding=utf-8
import sys


def operate(dict_, res, values):
    # res[values[1]] += values[2]
    now = res[values[1]] + values[2]
    if now > dict_[values[1]]:
        res[values[1]] = dict_[values[1]]
        values[2] = now - dict_[values[1]]
        if values[1]<len(dict_):
            values[1] += 1
            operate(dict_, res, values)
    else:
        res[values[1]] = res[values[1]] + values[2]

    return res


def answer(res, values):
    return res[values[1]]


if __name__ == "__main__":
    # 读取第一行的n,m
    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    volumes = list(map(int, line.split()))
    dict_ = {i+1:volumes[i] for i in range(len(volumes))}
    res = {i+1:0 for i in range(len(volumes))}
    ans = 0
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        if len(values) == 2:
            ans = answer(res, values)
            print(ans)
        if len(values) == 3:
            res = operate(dict_, res, values)
