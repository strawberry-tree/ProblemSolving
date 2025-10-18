from collections import deque

def solution(maps):
    def bfs(sx, sy, ex, ey):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        dist = [[-1] * len(maps[0]) for _ in range(len(maps))]

        queue = deque([(sx, sy)])
        dist[sx][sy] = 0
        
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]        
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] != "X" and dist[nx][ny] == -1:
                        queue.append((nx, ny))
                        dist[nx][ny] = dist[cx][cy] + 1
                        
                        # 목적지 도착
                        if nx == ex and ny == ey:
                            return dist[nx][ny]
        
        return -1
                        
    # 시작점, 레버, 끝점 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                sx, sy = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j
    

    # 레버를 당기기 전
    time1 = bfs(sx, sy, lx, ly)
    time2 = bfs(lx, ly, ex, ey)
    
    if time1 == -1 or time2 == -1:
        return -1
    else:
        return time1 + time2
