from collections import deque

n = int(input())

# 미확인 시 None.
dp = [None] * (max(6, n + 1))
queue = deque([2, 5])
dp[2] = 1
dp[5] = 1

def bfs():
    while queue:
        curr = queue.popleft()
        if curr == n:
            return dp[curr]
        for coin in [2, 5]:
            adj = curr + coin
            if adj <= n and dp[adj] is None:
                dp[adj] = dp[curr] + 1
                queue.append(adj)
    return -1

print(bfs())