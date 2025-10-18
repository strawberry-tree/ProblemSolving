# 전형적인 bfs문제

from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    def bfs(sx, sy):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        dist = [[-1] * M for _ in range(N)]
        queue = deque([(sx, sy)])
        dist[sx][sy] = 1
        
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[cx][cy] + 1
                        
                        if nx == N - 1 and ny == M - 1:
                            return dist[nx][ny]
                        
                        queue.append((nx, ny))
        
        return -1
                        
    
    return bfs(0, 0)