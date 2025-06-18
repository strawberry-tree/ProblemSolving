import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (M + 2) for _ in range(N + 2)]
graph[0][0] = -1
# -1: 치즈 X, 치즈외부 공간
# 0: 치즈 X, 치즈내부 공간
# 1: 치즈 O

for i in range(1, N + 1):
    input_line = list(map(int, input().split()))
    for j in range(1, M + 1):
        graph[i][j] = input_line[j - 1]
        

cheeses = 0     # 치즈 수

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if graph[i][j] == 1:
            cheeses += 1

time = 0        # 몇 초?
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(sx, sy):
    queue = deque([(sx, sy)])
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    
    while queue:
        x, y = queue.popleft()
        
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N + 2 and 0 <= ny < M + 2:
                if graph[nx][ny] != 1 and not visited[nx][ny]:
                    graph[nx][ny] = -1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def if_melt(x, y):
    # 공기접촉횟수
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N + 2 and 0 <= ny < M + 2:
            if graph[nx][ny] == -1:
                count += 1
    if count >= 2:
        return True
    else:
        return False


while cheeses > 0:
    time += 1
    
    bfs(0, 0)
    melt = []
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j] == 1:
                if if_melt(i, j):
                    melt.append((i, j))
    for i, j in melt:
        graph[i][j] = -1
        cheeses -= 1
        
print(time)