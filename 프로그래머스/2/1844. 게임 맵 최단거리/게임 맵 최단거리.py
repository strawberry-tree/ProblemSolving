from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    distance = [[-1] * m for _ in range(n)] # -1은 미방문
    distance[0][0] = 1
    
    queue = deque([(0, 0)])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # (1) 범위 안?
            if 0 <= nx < n and 0 <= ny < m:
                # (2) 벽 없는 칸? (3) 미방문?
                if maps[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    # 목적지 도착
                    if nx == (n - 1) and ny == (m - 1):
                        return distance[nx][ny]
                    queue.append((nx, ny))
                    
    return -1