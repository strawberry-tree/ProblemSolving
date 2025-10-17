import math

def solution(n, stations, w):
    answer = 0
    
    cover_list = [(0, 0)]
    for s in stations:
        cover_list.append((max(1, s - w), min(n, s + w)))
    cover_list.append((n + 1, n + 1))
    
    print(cover_list)
    for i in range(len(cover_list) - 1):
        gap = (cover_list[i + 1][0] - cover_list[i][1] - 1)
        answer += math.ceil((gap) / (2 * w + 1))
    
    return answer