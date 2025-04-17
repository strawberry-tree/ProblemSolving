import heapq
from collections import defaultdict

def solution(N, road, K):
    # 인접 리스트로 그래프 구현
    graph = defaultdict(list)
    min_weight = defaultdict(lambda: float('inf')) # 중복된 간선 제거를 위한 딕셔너리
    for v1, v2, weight in road:
        if weight < min_weight[(v1, v2)]:
            min_weight[(v1, v2)] = weight
    for (v1, v2), weight in min_weight.items():
        graph[v1].append((v2, weight))
        graph[v2].append((v1, weight))
        
    # 다익스트라 알고리즘
    distance = [float('inf')] * (N + 1)
    distance[1] = 0
    queue = [(0, 1)]
    
    while queue:
        dist, curr = heapq.heappop(queue)
        if dist > distance[curr]:
            continue
        for (adj, adj_dist) in graph[curr]:
            new_dist = distance[curr] + adj_dist
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                heapq.heappush(queue, (new_dist, adj))
    
    # K 이하 시간인 경우 계산
    result = 0
    for i in range(1, N + 1):
        if distance[i] <= K:
            result += 1
    return result
