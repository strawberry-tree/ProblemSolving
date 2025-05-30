import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)


def bfs(start):
    q = deque([1])
    visited[1] = True

    while q:

        curr = q.popleft()
        for next in graph[curr]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

bfs(1)
print(sum(visited) - 1)

