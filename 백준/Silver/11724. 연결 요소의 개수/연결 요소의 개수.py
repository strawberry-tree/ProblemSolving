import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
     
answer = 0           
for i in range(1, N + 1):
    if not visited[i]:
        answer += 1
        bfs(i, graph, visited)
print(answer)