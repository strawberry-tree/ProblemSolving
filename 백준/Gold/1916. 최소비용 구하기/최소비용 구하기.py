import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = float('inf')
graph = [[] for _ in range(N + 1)] # 인접리스트
dist_table = [INF] * (N + 1)             # 거리 정보

# 인접 리스트 만들기: (노드, 가중치)
for _ in range(M):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

chulbal, dochak = map(int, input().split())

# 다익스트라 알고리즘
def djikstra(chulbal, dochak, graph, dist):
    queue = []
    
    # (최소비용, 노드)
    heapq.heappush(queue, (0, chulbal))
    dist_table[chulbal] = 0
    
    while queue:
        i_cost, i = heapq.heappop(queue)
        
        if i == dochak:
            return i_cost
        
        for j, j_cost in graph[i]:
            new_cost = i_cost + j_cost
            if new_cost < dist_table[j]:
                dist_table[j] = new_cost
                heapq.heappush(queue, (dist_table[j], j))
                
print(djikstra(chulbal, dochak, graph, dist_table))