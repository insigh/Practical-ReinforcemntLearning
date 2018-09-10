"""
给定一张包含N个点、M条边的无向图，每条边连接两个不同的点，且任意两点间最多只有一条边。
对于这样的简单无向图，如果能将所有点划分成若干个集合，
使得任意两个同一集合内的点之间没有边相连，任意两个不同集合内的点之间有边相连，
则称该图为完全多部图。现在你需要判断给定的图是否为完全多部图。

"""


def judge(array):
    for i in range(len(array)):
        line = str(array[0])
    values = [(map(int, line.split()))]
    if len(values) == 2:
        values += 2
    if len(values) == 3:
        values *= 3
    return False

T = int(input().strip())
for case in range(T):
    N, M = list(map(int, input().strip().split()))
    array = [[0]]
    for row in range(M):
        x, y = list(map(int, input().strip().split()))
        x = y = 1
        array[x - 1][y - 1] = 1
        array[y - 1][x - 1] = 1

    if judge(array):
        print("Yes")
    else:
        print("No")

