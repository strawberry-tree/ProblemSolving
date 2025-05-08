def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    
    for i in range(len(land)):
        for j in range(4):
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                max_prev = -float('inf')
                for k in range(4):
                    if k != j:
                        max_prev = max(max_prev, dp[i - 1][k])
                dp[i][j] = max_prev + land[i][j]
    
    return max(dp[-1])
    
    

    return answer