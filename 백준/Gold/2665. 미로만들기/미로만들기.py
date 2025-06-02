import heapq
import sys

input = sys.stdin.readline

N = int(input())
grid = []
INF = float('inf')
distance = [[INF] * N for _ in range(N)]

for _ in range(N):
    grid.append(list(map(int, input().strip())))

def djikstra():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    # 거리, x좌표, y좌표
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distance[0][0] = 0

    while queue:
        dist, x, y = heapq.heappop(queue)
        if distance[x][y] < dist:
            continue
        # 인접칸 거리갱신
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == 1:   # 흰 방
                    new_dist = dist
                else:
                    new_dist = dist + 1
                    
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heapq.heappush(queue, (new_dist, nx, ny))
    
djikstra()
print(distance[-1][-1])