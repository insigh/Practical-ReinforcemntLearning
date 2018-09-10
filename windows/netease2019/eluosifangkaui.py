"""
3 9
1 1 2 2 2 3 1 2 3
res : 2
"""

n, m = [ int(item) for item in input().split()]
numbers = [int(item) for item in input().split()]
dict_ = { i:0 for i in range(1,n+1)}
for num in numbers:
    if num in dict_.keys():
        dict_[num] += 1
print(min(dict_.values()))