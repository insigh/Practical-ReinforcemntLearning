"""
2 2 6
res : 'zzaa'
"""

n ,m, k = [int(item) for item in input().split()]
all_sub = []


def getall_sub(n, m, res):
    if m == 0 and n == 0:
        all_sub.append(res)
        return
    if m == 0:
        getall_sub(n-1, m, res+'a')
    if n == 0:
        getall_sub(n, m-1, res+'z')
    elif m>0 and n > 0:
        getall_sub(n-1, m, res+'a')
        getall_sub(n, m-1, res+'z')


getall_sub(n, m, '')
L = len(all_sub)
if k < 0 or k > L:
    print(-1)
else:
    print(all_sub[k-1])