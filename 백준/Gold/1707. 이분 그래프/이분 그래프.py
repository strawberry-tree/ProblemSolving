from collections import deque
import sys
input = sys.stdin.readline 
 

def check(graph):
    def bfs(x):
        queue = deque([x])
        visited[x] = 'A'
        
        while queue:
            i = queue.popleft()
            for j in graph[i]:
                if not visited[j]:
                   flag = 'B' if visited[i] == 'A' else 'A'
                   visited[j] = flag
                   queue.append(j)
                elif visited[j] == visited[i]:
                    return False
        
        return True
                
    N = len(graph) - 1    # 노드 수
    visited = [False] * (N + 1)
    
    for i in range(1, N + 1):
        if not visited[i]:
            if not bfs(i):
                return False

    return True

K = int(input())
for _ in range(K):
    
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    if check(graph):
        print("YES")
    else:
        print("NO")