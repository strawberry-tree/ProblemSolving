import sys
input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))
    
stack = []
for i in range(N - 1, -1, -1):    
    if len(stack) <= 0 or stack[-1] < nums[i]:
        stack.append(nums[i])

print(len(stack))