N = int(input())
memo = [None] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        memo[i] = 1
    elif i == 2:
        memo[i] = 2
    else:
        memo[i] = (memo[i - 1] + memo[i - 2]) % 15746

print(memo[N])