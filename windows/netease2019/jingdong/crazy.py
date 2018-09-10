"""
链接：https://www.nowcoder.com/questionTerminal/6995575f1eba4c0085180c0d5fbcd096
来源：牛客网

东东从京京那里了解到有一个无限长的数字序列: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, ...(数字k在该序列中正好出现k次)。东东想知道这个数字序列的第n项是多少,你能帮帮他么
"""

n = int(input().strip())


def Binary_search(n, L, R):
    mid = (L+R)//2
    if n <= (mid*(mid+1)//2) and n>(mid*(mid-1)//2):
        return mid
    elif n > (mid*(mid+1)//2):
        return Binary_search(n, mid+1, R)
    elif n < (mid*(mid-1)//2):
        return Binary_search(n, L, mid-1)


print(Binary_search(n, 1, 100000000000))