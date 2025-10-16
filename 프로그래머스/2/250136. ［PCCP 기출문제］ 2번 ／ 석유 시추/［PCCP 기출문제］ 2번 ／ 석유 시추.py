from collections import deque


    

def solution(land):
    # 열별로 뽑을 수 있는 석유량의 수
    N, M = len(land), len(land[0])
    oil_list = [0] * M
    visited = [[False] * M for _ in range(N)]
    
    def grid_bfs(sx, sy):
        N, M = len(land), len(land[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        queue = deque([(sx, sy)])
        visited[sx][sy] = True
        total_oil = 1
        ok_cols = set([sy])

        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    ok_cols.add(ny)
                    visited[nx][ny] = True
                    total_oil += 1

        for col in ok_cols:
            oil_list[col] += total_oil  

    
    # 모든 칸 순회하며, 석유가 뭍힌 땅 중 미방문 땅 있을 시 거기서부터 탐색
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and not visited[i][j]:
                grid_bfs(i, j)
    
            
    answer = max(oil_list)
    return answer