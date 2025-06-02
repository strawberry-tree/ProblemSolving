import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(prev, curr):
    parent[curr] = prev
    visited[curr] = True
    for i in graph[curr]:
        if not visited[i]:
            dfs(curr, i)
    
dfs(None, 1)

for i in range(2, N + 1):
    print(parent[i])