import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
wine = [0]

for _ in range(N):
    wine.append(int(input()))

for i in range(1, N + 1):
    if i == 1:
        dp[i] = wine[1]
    elif i == 2:
        dp[i] = wine[1] + wine[2]
    else:
        dp[i] = max(wine[i] + dp[i - 2], wine[i] + wine[i - 1] + dp[i - 3], dp[i - 1])
        
print(max(dp))