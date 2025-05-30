# BFS를 사용
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)
n, m = map(int, input().split())
grid = []
depth = [[-1] * m for _ in range(n)]

for x in range(n):
    grid.append(list(map(int, input())))

def bfs(x, y):
    queue = deque([(x, y)])
    depth[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and depth[nx][ny] == -1:
                queue.append((nx, ny))
                depth[nx][ny] = depth[x][y] + 1

bfs(0, 0)
print(depth[n-1][m-1])
