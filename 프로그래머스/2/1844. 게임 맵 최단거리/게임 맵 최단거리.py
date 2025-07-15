from collections import deque
      
def solution(maps):                
    N = len(maps)                           # 행의 수
    M = len(maps[0])                        # 열의 수
    
    # 미방문 시 -1. 방문 시 distance.
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 1                       # 시작 칸도 한 칸으로 침.
    queue = deque([(0, 0)])
    dx = [-1, 0, 1, 0]                      # 좌우 이동
    dy = [0, -1, 0, 1]                      # 상하 이동

    while queue:
        cx, cy = queue.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 맵 안의 칸인가? 벽이 없는가? 방문하지 않은 칸인가?
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
                
    return visited[-1][-1]