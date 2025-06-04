from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

def make_graph():
    n = int(input())
    ranks = list(map(int, input().split()))
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    for i in range(n):
        for j in range(i + 1, n):
            a = ranks[i]
            b = ranks[j]
            graph[a][b] = True
            indegree[b] += 1
    
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        
        if graph[a][b]:
            graph[a][b], graph[b][a] = False, True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b], graph[b][a] = True, False
            indegree[b] += 1
            indegree[a] -= 1
            
    def top_sort(n, graph, indegree):
        result = []
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
        
        
        while queue:
            x = queue.popleft()
            result.append(str(x))
            for y in range(1, n + 1):
                if graph[x][y]:
                    indegree[y] -= 1
                    if indegree[y] == 0:
                        queue.append(y)
        
        if len(result) != n:
            return "IMPOSSIBLE"
        else:
            return " ".join(result)    
    
    return top_sort(n, graph, indegree)

for _ in range(T):
    print(make_graph()) 
    
