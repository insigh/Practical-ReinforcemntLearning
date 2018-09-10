"""
5
2 7 3 4 9
3
1 25 11

"""

n = int(input())
numbers = [int(item) for item in input().split()]
m = int(input())
queries = [int(item) for item in input().split()]
aggregate = [numbers[0]]
count = numbers[0]
for num in numbers[1:]:
    count += num
    aggregate.append(count)


def BinarySearch(key,c):
    lo,hi= 0,len(c)-1
    while lo <= hi:
        # print(lo, hi)
        mid = int(hi+lo)//2
        # print(mid)
        if key<c[mid] and mid>0:
            if key <= c[mid-1]:
                hi = mid-1
            elif key>c[mid-1]:
                return mid
        elif key>c[mid]:
            if key >= c[mid+1]:
                lo = mid+1
            elif key<c[mid+1]:
                return mid+1
        else:
            return mid


for query in queries:
    print(BinarySearch(query, aggregate)+1)