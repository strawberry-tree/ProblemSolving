def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]

    # 첫행은 그대로
    dp[0] = land[0]
    
    # 둘째 행부터
    for i in range(len(dp)):
        for j in range(4):
            dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
            dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][1]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][2]
            dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][3]
    return max(dp[-1])