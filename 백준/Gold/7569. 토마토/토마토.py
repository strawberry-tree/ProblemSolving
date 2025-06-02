from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
queue = deque()

for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    graph.append(box)

# 익은 토마토의 좌표를 바로 큐에 넣기
# 안 익은 토마토의 수 계산

tomatoes = 0
for x in range(H):
    for y in range(N):
        for z in range(M):
            if graph[x][y][z] == 1:
                # x좌표, y좌표, z좌표, 익는데 걸린 일수
                queue.append((x, y, z, 0))
            elif graph[x][y][z] == 0:
                tomatoes += 1

# 큐에서 토마토를 꺼내면
# 양옆의 토마토가 익음
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    x, y, z, time = queue.popleft()
    
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        
        # 인접한 익지 않은 토마토를 익힘
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1
                
                # 익은 토마토의 좌표 + 시간
                queue.append((nx, ny, nz, time + 1))
                tomatoes -= 1
                
# 토마토가 모두 익지 못함
if tomatoes != 0:
    print(-1)
# 토마토가 모두 익음: 마지막 토마토가 익은 시간
else:
    print(time)