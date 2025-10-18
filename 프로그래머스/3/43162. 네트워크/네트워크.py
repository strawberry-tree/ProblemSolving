from collections import deque

def solution(n, computers):
    visited = [False] * (n)
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            curr = queue.popleft()
            for adj in range(n):
                if computers[curr][adj] == 1:
                    if curr != adj and not visited[adj]:
                        visited[adj] = True
                        queue.append(adj)
                        
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer