import math
from collections import deque

def solution(progresses, speeds):
    days_list = deque()
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        days_list.append(days)
        
    answer = []
    
    while days_list:
        day = days_list.popleft()
        count = 1
        while days_list and days_list[0] <= day:
            days_list.popleft()
            count += 1
        answer.append(count)
    
    
    return answer