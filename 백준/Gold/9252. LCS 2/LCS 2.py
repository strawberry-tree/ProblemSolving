str_1 = input()
str_2 = input()

N = len(str_1)
M = len(str_2)

dp = [[""] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if str_1[i - 1] == str_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + str_1[i - 1]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
               
print(len(dp[N][M])) 
print(dp[N][M])