"""
链接：https://www.nowcoder.com/questionTerminal/0c564191e8c24f35a784a9363868ea09
来源：牛客网

东东对幂运算很感兴趣,在学习的过程中东东发现了一些有趣的性质: 9^3 = 27^2, 2^10 = 32^2
东东对这个性质充满了好奇,东东现在给出一个整数n,希望你能帮助他求出满足 a^b = c^d(1 ≤ a,b,c,d ≤ n)的式子有多少个。
例如当n = 2: 1^1=1^1
1^1=1^2
1^2=1^1
1^2=1^2
2^1=2^1
2^2=2^2
一共有6个满足要求的式子
"""
# import math
n = int(input().strip())

powers = {}
for i in range(1, n+1):
    for j in range(1, n+1):
        power = i**j
        v = powers.get(power, 0)
        powers[power] = v+1
nums = 0
for value in powers.values():
    nums += value**2
print(nums)
