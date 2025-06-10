import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i in (1, 2, 3):
            answer = 1
        elif i in (4, 5):
            answer = 2
        else:
            answer = dp[i - 1] + dp[i - 5]
        dp[i] = answer
    print(dp[n])