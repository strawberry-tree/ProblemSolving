N = int(input())

# dp[i][j]: j로 끝나는, i자리 계단 수 
dp = [[0] * 10 for _ in range(N + 1)]
rem = 1_000_000_000

for i in range(1, N + 1):
    if i == 1:
        for j in range(1, 10):
            dp[i][j] = 1
    else:
        dp[i][0] = dp[i - 1][1] % rem
        for j in range(1, 9):
            dp[i][j] = (dp[i - 1][j - 1] % rem + dp[i - 1][j + 1] % rem) 
        dp[i][9] = dp[i - 1][8] % rem

print(sum(dp[N]) % rem)