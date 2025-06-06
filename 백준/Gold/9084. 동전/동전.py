import sys
input = sys.stdin.readline

def do_dp():
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    for i in range(N):
        dp[i][0] = 1
    
    for i in range(1, N + 1):
        value = coins[i - 1]
        for j in range(1, M + 1):
            rem = j
            while rem >= 0:
                dp[i][j] += dp[i-1][rem]
                rem -= value
                
    print(dp[N][M])

T = int(input())
for _ in range(T):
    do_dp()
