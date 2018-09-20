"""
1 10
"""
a, b = list(map(int, input().strip().split()))

import time
def count_lucky(a, b):
    start = time.time()
    count = 0
    for i in range(a, b+1):
        i = str(i)
        lucky = True
        for j in range(len(i)//2):
            if i[j] == i[len(i)-j-1]:
                lucky = False
                break
            else:
                continue

        if lucky:
            count += 1
    end = time.time()
    print(end-start)
    return count


print(count_lucky(a, b))