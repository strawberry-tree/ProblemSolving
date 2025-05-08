def solution(triangle):
    dp = [[triangle[0][0]]]
    
    for i in range(1, len(triangle)):
        dp_row = []
        for j in range(i + 1):
            if j == 0:
                dp_elem = dp[i - 1][0]
            elif j == i:
                dp_elem = dp[i - 1][j - 1]
            else:
                dp_elem = max(dp[i - 1][j - 1], dp[i - 1][j])
            dp_row.append(dp_elem + triangle[i][j])
        dp.append(dp_row)
    return max(dp[-1])