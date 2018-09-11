num = input().strip()
flag = True

if num[0] == '-':
    flag = False
num = num[::-1]
res = ''
if flag:
    i = 0
    while i < len(num) and num[i] == '0':
        i += 1
    res = ''.join(num[i:])
else:
    res
    i = 0
    while i < len(num)-1 and num[i] == '0':
        i += 1
    res = ''.join(num[i:-1])
    res = '-' + res
if res == '-' or res == '':
    print(0)
else:
    print(int(res))

