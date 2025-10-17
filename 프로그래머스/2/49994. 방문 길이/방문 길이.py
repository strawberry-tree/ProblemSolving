def solution(dirs):
    dx = {"U": 0, "D": 0, "L": -1, "R": 1}      # x축이동
    dy = {"U": 1, "D": -1, "L": 0, "R": 0}      # y축이동
    cx, cy = 0, 0
    visited = set()
    
    for d in dirs:
        nx, ny = cx + dx[d], cy + dy[d]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((cx, cy, nx, ny))
            visited.add((nx, ny, cx, cy))
            cx, cy = nx, ny
            
    
    return len(visited) // 2