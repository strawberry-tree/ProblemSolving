import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
dist_table = [float('inf')] * (V + 1)

for _ in range(E):
    # u->v, 가중치w
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
def dijkstra(start):
    queue = []
    # (가중치, 노드번호)
    heapq.heappush(queue, (0, start))
    dist_table[start] = 0
    
    while queue:
        i_dist, i = heapq.heappop(queue)
        if i_dist > dist_table[i]:
            continue
        for j, j_dist in graph[i]:
            total_dist = i_dist + j_dist
            if total_dist < dist_table[j]:
                dist_table[j] = total_dist
                heapq.heappush(queue, (total_dist, j))
                
dijkstra(K)

for i in range(1, V + 1):
    result = dist_table[i]
    
    if result >= float('inf'):
        print("INF")
    else:
        print(result)
   