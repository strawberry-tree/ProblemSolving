def solution(triangle):
    dp = [[0] * (i) for i in range(1, len(triangle) + 1)]
    
    # 1층: triangle과 동일
    dp[0][0] = triangle[0][0]
    
    # 2층부터
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            # 맨 왼쪽
            if j == 0:
                dp[i][0] = dp[i-1][0] + triangle[i][0]
            elif j == i:
                dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[-1])