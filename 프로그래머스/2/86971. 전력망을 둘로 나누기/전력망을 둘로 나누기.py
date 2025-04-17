from collections import defaultdict, deque

def solution(n, wires):
    graph = defaultdict(list)
    min_diff = float('inf')
    
    # 인접 리스트
    for (v1, v2) in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # bfs - 잘린 선 제외
    def bfs(node, v1, v2):
        visited = set([node])
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for adj in graph[curr]:
                if {curr, adj} != {v1, v2}:
                    if adj not in visited:
                        visited.add(adj)
                        queue.append(adj)
        return len(visited)
        
    # 각 와이어를 자를 때 bfs 수행하고 탑 수 차이 비교
    for (v1, v2) in wires:
        oneside = bfs(1, v1, v2)
        otherside = n - oneside
        diff = abs(oneside - otherside)
        min_diff = min(min_diff, diff)
    
    return min_diff