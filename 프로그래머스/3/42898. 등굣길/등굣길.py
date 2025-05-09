def solution(m, n, puddles):
    puddles = set((y, x) for x, y in puddles)
    paths = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) in puddles:
                paths[i][j] = 0
            elif i == 1 and j == 1:
                paths[i][j] = 1
            else:
                paths[i][j] = (paths[i-1][j] + paths[i][j-1]) % 1000000007
    return paths[n][m]