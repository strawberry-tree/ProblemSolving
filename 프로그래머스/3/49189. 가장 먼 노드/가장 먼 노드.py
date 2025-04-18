from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for (v1, v2) in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    def bfs(start):
        queue = deque([(start, 0)])
        visited = set([start])
        curr_dist = 0   # 가장 멀리 떨어진 거리
        count = 0       # 가장 멀리 떨어진 노드 수
        
        while queue:
            curr, dist = queue.popleft()
            
            # 가장 멀리 떨어진 거리 갱신
            if dist > curr_dist:
                curr_dist = dist
                count = 1
            else:
                count += 1
                
            for adj in graph[curr]:
                if adj not in visited:
                    queue.append((adj, dist + 1))
                    visited.add(adj)
        
        return count
        
    return bfs(1)