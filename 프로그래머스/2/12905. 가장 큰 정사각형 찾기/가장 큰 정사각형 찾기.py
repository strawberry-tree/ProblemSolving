def solution(board):
    N, M = len(board), len(board[0])
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # i행j열이 오른쪽 아래 칸인, 제일 큰 정사각형의 한 변 길이
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if board[i-1][j-1] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            answer = max(answer, dp[i][j])
    
    return answer ** 2