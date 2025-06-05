from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
visited = [[False] * M for _ in range(N)]

for _ in range(N):
    grid.append(list(input()))
    
count = 0
dxdy = [-1, 1]

def bfs(sx, sy, shape):
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            if shape == "-":
                nx, ny = x, y + dxdy[i]
            else:
                nx, ny = x + dxdy[i], y
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] == shape:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j, grid[i][j])
            count += 1
            
print(count)