import sys
input = sys.stdin.readline

def do_dp():
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1
    
    for c in coins:
        for i in range(M + 1):
            if i + c <= M:
                dp[i + c] += dp[i]

    print(dp[M])

T = int(input())
for _ in range(T):
    do_dp()