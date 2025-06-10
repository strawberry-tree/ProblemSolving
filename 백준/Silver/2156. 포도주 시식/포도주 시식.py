import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 3 for _ in range(N)]
wine = []

for _ in range(N):
    wine.append(int(input()))

for i in range(N):
    if i == 0:
        dp[i][0] = wine[i]
        dp[i][1] = wine[i]
    else:
        dp[i][0] = dp[i - 1][1] + wine[i]
        dp[i][1] = dp[i - 1][2] + wine[i]
        dp[i][2] = max(dp[i - 1])

print(max(dp[-1]))