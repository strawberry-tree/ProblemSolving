


def solution(board):
    
    def check_danger(x, y):
        # 지뢰가 매설된 칸 및 인접 8칸을 위험 지역 처리
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        
        # 지뢰가 매설된 칸
        safe[x][y] = False

        # 인접 8칸
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                safe[nx][ny] = False
    
    N = len(board)              # 배열의 한 변 길이
    safe = [[True] * N for _ in range(N)]   # 안전: True, 위험: False
    
    # 모든 칸 순회
    for i in range(N):
        for j in range(N):
            # 지뢰를 발견하면, 해당 칸 및 인접 8칸을 위험 처리
            if board[i][j] == 1:
                check_danger(i, j)
    
    # safe인 칸 확인
    answer = 0
    for i in range(N):
        for j in range(N):
            if safe[i][j]:
                answer += 1
    
    return answer 