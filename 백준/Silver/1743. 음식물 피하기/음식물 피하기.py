from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True    # 아차차 이걸 까먹을 뻔.
    count = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        cx, cy = queue.popleft()
        count += 1
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    return count


N, M, K = map(int, input().split())
answer = 0

# 각 칸의 방문 여부
# 음식물이 없는 칸은 True.
# 음식물이 있는 칸은 방문 전 False, 방문 후 True.
visited = [[True] * (M) for _ in range(N)]

# 음식물이 떨어진 위치
marks = []
for _ in range(K):
    x, y = map(int, input().split())
    marks.append((x - 1, y - 1))
    visited[x - 1][y - 1] = False

# 음식물 떨어진 위치 - 미방문시 BFS로 방문 처리\
for x, y in marks:
    if not visited[x][y]:
        count = bfs(x, y)
        answer = max(answer, count)

print(answer)