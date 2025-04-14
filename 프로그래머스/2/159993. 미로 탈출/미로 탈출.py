from collections import deque

# 시작위치 찾기
def find_start(maps):
    # O(N * M)
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                return (i, j)

# 특정 위치에서 목적지까지 최단 거리
def find_target(maps, sx, sy, target):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 이동시간 저장 용도
    grid = [[-1] * m for _ in range(n)]
    grid[sx][sy] = 0
        
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()
        if maps[x][y] == target:
            return (grid[x][y], x, y)
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != "X" and grid[nx][ny] == -1:
                    queue.append((nx, ny))
                    grid[nx][ny] = grid[x][y] + 1
    
    return None

def solution(maps):
    sx, sy = find_start(maps)
    result_l = find_target(maps, sx, sy, "L")
    if result_l is None:
        return -1
    result_e = find_target(maps, result_l[1], result_l[2], "E")
    if result_e is None:
        return -1
    
    result = result_l[0] + result_e[0]
    return result
                
