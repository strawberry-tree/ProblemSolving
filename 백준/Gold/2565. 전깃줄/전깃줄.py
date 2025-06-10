import sys
input = sys.stdin.readline

N = int(input())
ropes = []

for _ in range(N):
    ropes.append(tuple(map(int, input().split())))
ropes.sort()

dp = [1] * N

for i in range(N):
    prev_max = 0
    for j in range(i):
        if ropes[j][1] < ropes[i][1]:
            prev_max = max(prev_max, dp[j])
    dp[i] += prev_max
    
print(N - max(dp))