# coding=utf-8
import sys


def solve(N, M):
    if M == 0 or N == 0:
        return 0

    if N == 1:
        if M == 1:
            return 1
        elif M >= 2:
            return M -2

    if N >= 2:
        if M == 1:
            return N -2
        else:
            return (M-2)*(N-2)




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
        print(ans)