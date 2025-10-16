def solution(mats, park):
    x_len = len(park)
    y_len = len(park[0])
    
    dp = [[0] * (len(park[0]) + 1) for _ in range(len(park) + 1)]
    
    max_side = 0
    
    for x in range(1, x_len + 1):
        for y in range(1, y_len + 1):
            if park[x-1][y-1] != "-1":
                dp[x][y] = 0
            else:
                dp[x][y] = min(dp[x-1][y-1], dp[x][y-1], dp[x-1][y]) + 1
                max_side = max(max_side, dp[x][y])
    
    print(dp)
    print(max_side)
    
    mats.sort(reverse=True)
    for m in mats:
        if m <= max_side:
            return m
    return -1