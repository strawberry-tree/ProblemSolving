import sys
input = sys.stdin.readline

N = int(input())
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))
    
moves = [[0] * N for _ in range(N)]
moves[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(moves[-1][-1])
        else:
            if i + grid[i][j] < N:
                moves[i + grid[i][j]][j] += moves[i][j]
            if j + grid[i][j] < N:
                moves[i][j + grid[i][j]] += moves[i][j]