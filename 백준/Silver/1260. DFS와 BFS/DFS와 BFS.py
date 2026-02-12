from collections import defaultdict, deque
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)

N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 정점 번호 작은 순으로 방문 위함
for i in range(1, N + 1):
    graph[i].sort()
    
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(curr):
    print(curr, end=" ")
    visited_dfs[curr] = True
    for adj in graph[curr]:
        if not visited_dfs[adj]:
            dfs(adj)
            
def bfs(start):
    visited_bfs[start] = True
    queue = deque([start])
    
    while queue:
        curr = queue.popleft()
        print(curr, end=" ")
        for adj in graph[curr]:
            if not visited_bfs[adj]:
                visited_bfs[adj] = True
                queue.append(adj)
                

dfs(V)
print()
bfs(V)