from collections import deque

def solution(n, computers):
    visited = set()
    count = 0
    
    def bfs(n):
        queue = deque([n])
        visited.add(n)
        
        while queue:
            curr_i = queue.popleft()
            for next_i, connected in enumerate(computers[curr_i]):
                if next_i != curr_i and connected == 1 and next_i not in visited:
                    queue.append(next_i)
                    visited.add(next_i)
    
    for node in range(n):
        if node not in visited:
            bfs(node)
            count += 1

    return count