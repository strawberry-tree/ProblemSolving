from collections import deque
import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**9)
 
def check(graph):
    def dfs(i, flag):
        visited[i] = flag
        for j in graph[i]:
            if not visited[j]:
                if flag == "A":
                    result = dfs(j, "B")
                elif flag == "B":
                    result = dfs(j, "A")
                if not result:
                    return False        
            elif visited[j] == flag:
                return False

        return True
            
                
    N = len(graph) - 1    # 노드 수
    visited = [False] * (N + 1)
    
    for i in range(1, N + 1):
        if not visited[i]:
            if not dfs(i, 'A'):
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