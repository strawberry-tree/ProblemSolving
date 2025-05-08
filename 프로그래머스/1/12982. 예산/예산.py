import heapq

def solution(d, budget):
    result = 0
    heapq.heapify(d)
    while d:
        money = heapq.heappop(d)
        if budget - money >= 0:
            budget -= money
            result += 1
        else:
            break
    return result