import sys
input = sys.stdin.readline

# N행, M열
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
    
DP = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

# 0행을 채우기
for j in range(M):
    for k in range(3):
        DP[0][j][k] = grid[0][j]
        
# 1행부터 채우기
for i in range(1, N):
    for j in range(M):
        # 왼쪽 아래로 내려온 경우
        if j != M - 1:
            DP[i][j][0] = min(DP[i - 1][j + 1][1], DP[i - 1][j + 1][2]) + grid[i][j]
        
        # 가운데 아래로 내려온 경우
        DP[i][j][1] = min(DP[i - 1][j][0], DP[i - 1][j][2]) + grid[i][j]
        
        # 오른쪽 아래로 내려온 경우
        if j != 0:
            DP[i][j][2] = min(DP[i - 1][j - 1][0], DP[i - 1][j - 1][1]) + grid[i][j]

# 정답 구하기
answer = min(min(DP[N - 1][j][k] for k in range(3)) for j in range(M))
print(answer)