import sys
N, M = map(int, input().split())
input = sys.stdin.readline

INF = float('inf')
graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = False

for _ in range(M):
    heavy, light = map(int, input().split())
    graph[heavy][light] = True 

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not graph[i][j]:
                graph[i][j] = graph[i][k] and graph[k][j]
            
answer = 0
for i in range(1, N + 1):
    # 더 가벼운 게 몇 개?
    row_check = sum(graph[i][j] for j in range(1, N + 1))
    
    # 더 무거운 게 몇 개?
    col_check = sum(graph[j][i] for j in range(1, N + 1))
    
    if row_check >= (N + 1) // 2 or col_check >= (N + 1) // 2:
        answer += 1

print(answer)
    