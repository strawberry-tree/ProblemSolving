from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1, len(order) - 1):
        graph[order[i]].append(order[i + 1])
        indegree[order[i + 1]] += 1

queue = deque()   
    
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        
result = []
while queue:
    i = queue.popleft()
    result.append(i)
    for j in graph[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)