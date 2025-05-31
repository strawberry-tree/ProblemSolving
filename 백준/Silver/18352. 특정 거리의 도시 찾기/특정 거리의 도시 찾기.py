from collections import deque
import sys

input = sys.stdin.readline

# 도시, 도로, 목표 최단거리, 출발 도시
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 인접 리스트
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
# 각 도시의 거리정보. 미방문 시 None
dist = [None] * (N + 1)

def bfs(graph, start, dist):
    dist[start] = 0     # 출발 도시의 경로는 0
    queue = deque([start])

    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if dist[j] is None:
                # 인접 도시의 거리는
                # 현재 도시의 거리 + 1로 계산
                dist[j] = dist[i] + 1
                queue.append(j)    

bfs(graph, X, dist)

# 최단 거리가 K
count = 0

for i in range(1, N + 1):
    if dist[i] == K:
        print(i)
        count += 1

if count == 0:
    print(-1)