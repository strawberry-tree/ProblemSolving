from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []

for _ in range(R):
    graph.append(list(input()))
    
# 각 칸의 도착 여부
visited = [[False] * C for _ in range(R)] 

# N초부터 물이 차 있음
# 물이 차지 않은 경우, INF
INF = float('inf')
water = [[INF] * C for _ in range(R)]
water_queue = deque()

for x in range(R):
    for y in range(C):
        if graph[x][y] == "S":
            sx, sy = x, y       # 시작 좌표
        elif graph[x][y] == "*":
            water_queue.append((x, y))
            water[x][y] = 1
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
        
# water 채우기 위해 BFS
while water_queue:
    x, y = water_queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if water[nx][ny] == INF and graph[nx][ny] not in {"X", "D"}:
                water[nx][ny] = water[x][y] + 1
                water_queue.append((nx, ny))

# 고슴도치의 이동
def move_dochi():
    dochi_queue = deque([(sx, sy, 1)])
    while dochi_queue:
        x, y, time = dochi_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and graph[nx][ny] not in {"X"} and water[nx][ny] > time + 1:
                    if graph[nx][ny] == "D":
                        return time
                    visited[nx][ny] = True
                    dochi_queue.append((nx, ny, time + 1))
    
    return "KAKTUS"

print(move_dochi())                