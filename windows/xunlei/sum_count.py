"""
给定整数n，取若干个1到n的整数可求和等于整数m，编程求出所有组合的个数。
比如当n=6，m=8时，
有四种组合：
[2,6], [3,5], [1,2,5], [1,3,4]。限定n和m小于120
输入描述:
整数n和m
"""

n, m = list(map(int, input().strip().split()))
dp = [[1 if i == 0 else 0 for i in range(m+1)] for j in range(n+1)]

for row in range(1, n+1):
    for col in range(1, m+1):
        if col - row < 0:
            dp[row][col] = dp [row-1][col]
        else:
            dp[row][col] = dp[row - 1][col] + dp[row-1][col-row]
print(dp[n][m])




def findallsolution(seek, res, i):
    global count
    if res == seek:
        count += 1
        return

    elif res > seek or i > n:
        return
    else:
        findallsolution(seek, res+i, i+1)
        findallsolution(seek, res, i+1)


# findallsolution(m, 0, 1)
# print(count)