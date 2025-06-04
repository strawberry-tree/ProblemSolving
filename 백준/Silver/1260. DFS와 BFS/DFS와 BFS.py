from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = []
unvisited_s = [i for i in range(1, N+1)]
result_s = []
queue = deque()
unvisited_q = [i for i in range(1, N+1)]
result_q = []

stack.append(V)
unvisited_s.remove(V)

while stack:
    p = stack[-1]
    if p not in result_s:
        result_s.append(p)
    dt = None
    for d in sorted(graph[p]):
        if d in unvisited_s:
            dt = d
            break
    if dt:
        stack.append(dt)
        unvisited_s.remove(dt)
    else:
        stack.pop()


queue.append(V)
unvisited_q.remove(V)

while queue:
    p = queue.popleft()
    result_q.append(p)
    for d in sorted(graph[p]):
        if d in unvisited_q:
            queue.append(d)
            unvisited_q.remove(d)

print(' '.join(map(str, result_s)))
print(' '.join(map(str, result_q)))




