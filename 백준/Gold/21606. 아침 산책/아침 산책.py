import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())

# 1 실내 0 실외
in_out = [0] + list(map(int, input().strip()))
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(i, curr):
    global count
    visited[i] = True
    
    # 실내인 경우
    if in_out[i] == 1:
        count += 2 * len(curr)
        for j in graph[i]:
            if not visited[j]:
                dfs(j, {i})
        curr.add(i)
        return curr

    # 실외인 경우
    else: 
        for j in graph[i]:
            if not visited[j]:
                curr = dfs(j, curr)
        return curr
    
dfs(1, set())
print(count)