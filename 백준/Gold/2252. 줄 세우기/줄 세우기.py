from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    # 학생 A가 학생 B 앞에 서야 됨
    # 즉, 노드 A -> 노드 B 방향의 간선이 존재함
    
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topsort():
    queue = deque()
    
    for i in range(1, N + 1):
        if indegree[i] == 0:    
            queue.append(i)

    while queue:
        curr = queue.popleft()
        print(curr, end=" ")
        for i in graph[curr]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)                    

topsort()