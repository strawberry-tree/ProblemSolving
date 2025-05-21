import math

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))
    
gaps = []

for i in range(N - 1):
    gaps.append(nums[i + 1] - nums[i])

div = math.gcd(*gaps)

answer = 0
for g in gaps:
    answer += (g // div - 1)
    
print(answer)