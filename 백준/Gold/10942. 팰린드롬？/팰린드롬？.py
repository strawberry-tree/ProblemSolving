import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
DP = [[True] * (N + 1) for _ in range(N + 1)]
    
for gap in range(1, N):
    for x in range(1, N - gap + 1):
        y = x + gap
        if nums[x - 1] == nums[y - 1] and DP[x + 1][y - 1]:
            DP[x][y] = True
        else:
            DP[x][y] = False
            
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(int(DP[S][E]))