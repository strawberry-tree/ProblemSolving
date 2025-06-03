from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    grid.append(list(map(int, input().split())))
            
def bfs(sx, sy, visited, memo):
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] >= 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny)) 
                elif grid[nx][ny] == 0:
                    memo[(x, y)] += 1
            
def get_answer():
    time = 0
    while True:
        count = 0
        visited = [[False] * M for _ in range(N)]
        memo = defaultdict(int)
        
        for x in range(N):
            for y in range(M):
                if grid[x][y] >= 1 and not visited[x][y]:
                    count += 1
                    if count >= 2:
                        return time
                    bfs(x, y, visited, memo)
                      
        if count == 0:
            return 0              

        for x, y in memo:
            grid[x][y] = max(grid[x][y] - memo[(x, y)], 0)
        time += 1
        
print(get_answer())         