
def dfs(m, n, k, res, temp):
    if m == n == k == 0 :
        if temp not in res:
            res.append(temp)
        return

    if m > 0:
        if temp:
            if temp[-1] != 'red':
                dfs(m-1, n, k, res, temp + ['red'])
        else:
            dfs(m - 1, n, k, res, temp + ['red'])
    if n > 0:
        if temp:
            if temp[-1] != 'blue':
                dfs(m, n - 1, k, res, temp + ['blue'])
        else:
            dfs(m, n-1, k, res, temp + ['blue'])
    if k > 0:
        if temp:
            if temp[-1] != 'green':
                dfs(m, n, k-1, res, temp + ['green'])
        else:
            dfs(m, n, k - 1, res, temp + ['green'])


def main():
    m, n, k = list(map(int, input().strip().split()))
    res = []
    dfs(m, n, k, res, [])
    print(len(res))


main()