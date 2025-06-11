from collections import deque

N = int(input())
dp = [None] * (N + 1)
dp[1] = 0

queue = deque([1])

while queue:
    curr = queue.popleft()
    if curr == N:
        print(dp[curr])
        break

    for adj in [curr + 1, curr * 2, curr * 3]:
        if adj <= N and dp[adj] is None:
            dp[adj] = dp[curr] + 1
            queue.append(adj)
            
 
result = []
curr = N
while dp[curr] != 0:
    result.append(curr)
    if curr % 3 == 0 and dp[curr // 3] == dp[curr] - 1:
        curr = curr // 3 
    elif curr % 2 == 0 and dp[curr // 2] == dp[curr] - 1:
        curr = curr // 2
    elif dp[curr - 1] == dp[curr] - 1:
        curr = curr - 1
        
result.append(1)
print(*result)