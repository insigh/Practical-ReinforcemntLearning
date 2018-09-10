"""
6
1 0
1 1
2 0
2 1
2 2
6 4
"""

# coding=utf-8
import sys


def solve(house_num, lived):
    if house_num < 3 or lived < 2:
        return (0, 0)
    min_ = 0
    if house_num - lived >= lived:
        return (min_, lived-1)
    elif house_num - lived < lived:
        return (min_, house_num - lived)


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        ans = solve(values[0], values[1])
        print(ans[0], ans[1])


