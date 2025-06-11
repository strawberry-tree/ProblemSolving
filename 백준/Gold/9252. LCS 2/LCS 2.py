str_1 = input()
str_2 = input()

N = len(str_1)
M = len(str_2)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if str_1[i - 1] == str_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
               
i = N
j = M
result = []

while i > 0 and j > 0: 
    if str_1[i - 1] == str_2[j - 1]:
        result.append(str_1[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(dp[N][M])
print("".join(reversed(result)))