import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0 for j in range(N + 1)] for i in range(N + 1)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        matrix[i+1][j+1] = matrix[i+1][j] + matrix[i][j+1] + row[j] - matrix[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = matrix[x2][y2] - (matrix[x2][y1-1] + matrix[x1-1][y2]) + matrix[x1-1][y1-1]
    print(result)