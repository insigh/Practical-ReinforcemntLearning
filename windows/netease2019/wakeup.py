"""
6 3
1 3 5 2 5 4
1 1 0 1 0 0
res : 16
"""

n, k = [int(item) for item in input().split()]
interests = [int(item) for item in input().split()]
wake = [int(item) for item in input().split()]
base = [interests[i]*wake[i] for i in range(len(wake))]
base = sum(base)
L = len(interests)
dict_ = {i: interests[i] for i in range(len(wake)) if wake[i] == 0}
keys = list(dict_.keys())
prev = dict_[keys[0]]
addition = sum([dict_[keys[i]] for i in range(0, k-1)])
print(addition)
for i in range(0, len(dict_)):
    if keys[i]+k < len(interests) and dict_.get(keys[i]+k) > prev:
        addition += dict_[keys[i]] - prev
        prev = dict_[keys[i]]
print(base+addition)







