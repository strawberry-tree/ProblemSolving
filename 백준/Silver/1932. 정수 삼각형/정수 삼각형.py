import sys
input = sys.stdin.readline

N = int(input())
grid = []
dp = [[0] * (i + 1) for i in range(N)]

for _ in range(N):
    grid.append(list(map(int, input().split())))

dp[0][0] = grid[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = grid[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = grid[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = grid[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            
print(max(dp[N - 1]))