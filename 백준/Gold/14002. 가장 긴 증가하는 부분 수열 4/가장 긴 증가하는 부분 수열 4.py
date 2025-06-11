N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N


for i in range(N):
    max_dp = 0
    for j in range(i):
        if nums[j] < nums[i]:
            max_dp = max(dp[j], max_dp)
    dp[i] += max_dp


answer = max(dp)
result = []

for i in range(N - 1, -1, -1):
    if dp[i] == answer:
        result.append(nums[i])
        answer -= 1

print(max(dp))
print(*reversed(result))