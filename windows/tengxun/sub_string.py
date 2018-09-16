"""
2
abab
ababab
"""

k = int(input().strip())
A = input().strip()
B = input().strip()

visited = []
count = 0
for i in range(0, len(A)-k+1):
    substring = A[i:i+k]
    if substring in visited:
        continue
    count += B.count(substring)
    visited.append(substring)

print(count)
