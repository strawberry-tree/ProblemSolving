from collections import deque

def find_start(maps):
    # O(N * M)
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                return (i, j)
            
def find_target(maps, sx, sy, target):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

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
    if result_l is not None:
        l_dist, lx, ly = result_l
    else:
        return -1
    
    result_e = find_target(maps, lx, ly, "E")
    if result_e is not None:
        e_dist, ex, ey = result_e
    else:
        return -1
    
    result = l_dist + e_dist
    return result
                