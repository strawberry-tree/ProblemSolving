import sys

# input
n, k = map(int, input().split())
grid = []

for row in range(n):
    grid.append(list(map(int, sys.stdin.readline().rstrip().split())))
s, x, y = map(int, input().split())

# 1초 전염 시작 위치
order = []
for a in range(n):
    for b in range(n):
        if grid[a][b] >= 1:
            order.append((grid[a][b], a, b))

# 전염 시뮬레이션 - 매초 전염 시작 위치 갱신
def bfs(order):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    order.sort()
    next_order = []
    
    while order:
        virusno, cx, cy = order.pop(0)
        for idx in range(4):
            nx, ny = cx + dx[idx], cy + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = virusno
                next_order.append((virusno, nx, ny))
    next_order.sort()

    return next_order

# 매초마다 전염
for _ in range(s):
    order = bfs(order)

# 정답 출력
answer = grid[x - 1][y - 1]
if answer < 1:
    answer = 0
print(answer)
