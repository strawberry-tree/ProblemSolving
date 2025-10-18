import heapq
from collections import defaultdict

def solution(N, road, K):
    # 마을1, 마을2, 가중치 (양방통행 가능)
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 다익스트라 알고리즘
    queue = []
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    # 가중치, 마을
    heapq.heappush(queue, (0, 1))
    
    while queue:
        cost, curr = heapq.heappop(queue)
        if cost > dist[curr]:
            continue
        
        for adj, adj_cost in graph[curr]:
            new_cost = cost + adj_cost
            if new_cost < dist[adj]:
                dist[adj] = new_cost
                heapq.heappush(queue, (new_cost, adj))
    
    # K 이하의 시간
    answer = sum(d <= K for d in dist[1:])

    return answer