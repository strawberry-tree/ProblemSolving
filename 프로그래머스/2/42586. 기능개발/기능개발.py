from collections import deque
from math import ceil

def solution(progresses, speeds):
    queue = deque()
    answer = []
    
    for p, s in zip(progresses, speeds):
        queue.append(ceil((100 - p) / s))
    
    while queue:
        k = queue.popleft()
        count = 1
        while queue and queue[0] <= k:
            queue.popleft()
            count += 1
        answer.append(count)
        
    return answer