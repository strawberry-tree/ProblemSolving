import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
queue = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)
    
while queue:
    curr = heapq.heappop(queue)
    print(curr, end=" ")
    for adj in graph[curr]:
        indegree[adj] -= 1
        if indegree[adj] == 0:
            heapq.heappush(queue, adj)