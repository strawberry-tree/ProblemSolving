# 일단 끊고 한쪽에서 DFS/BFS?
from collections import deque, defaultdict

def bfs(n, wires):
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited = [False] * (n + 1)
    
    queue = deque([1])
    visited[1] = True
    count = 1
    
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True
                count += 1
    
    return count
    

def solution(n, wires):
    min_diff = float('inf')
    for i in range(len(wires)):
        cut_wires = wires[:i] + wires[i + 1:]
        num_tops = bfs(n, cut_wires)
        
        # num_tops와 n - num_tops의 차이
        diff = abs(num_tops * 2 - n)
        min_diff = min(min_diff, diff)
    
    return min_diff