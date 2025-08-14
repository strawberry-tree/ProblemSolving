from collections import deque

# 가로크기 N, 세로크기 M
N, M = map(int, input().split())

# grid / visited 배열 만들기
grid = []

for _ in range(M):
    grid.append(list(input()))

    
visited = [[False] * N for _ in range(M)]
answer = [0, 0]     # 하양, 파랑

def bfs(x, y, color):
    queue = deque([(x, y)])
    visited[x][y] = True
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    count = 0
    
    while queue:
        cx, cy = queue.popleft()
        count += 1
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    if color == "W":
        answer[0] += count ** 2
    else:
        answer[1] += count ** 2
    

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, grid[i][j])
            
print(*answer)
