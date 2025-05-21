from itertools import permutations

N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))
    
def calc_cost(route):
    route = [0, *route, 0]
    cost = 0
    for i in range(len(route) - 1):
        start, end = route[i], route[i + 1]
        if W[start][end] == 0:
            return None
        cost += W[start][end]
    return cost

answer = float('inf')
    
for route in permutations(range(1, N)):
    result = calc_cost(route)
    if result:
        answer = min(answer, result)
        
print(answer)