from itertools import permutations

# O(N)
def check_total_cost(perm):
    total_cost = 0
    
    # 첫 도시 -> 마지막 도시까지 비용
    for i in range(len(perm) - 1):
        cost = graph[perm[i]][perm[i + 1]]
        if cost == 0:
            return None
        total_cost += cost
        
    # 마지막 도시 -> 첫 도시로 돌아가는 비용
    cost = graph[perm[-1]][perm[0]]
    if cost == 0:
        return None
    total_cost += cost
    return total_cost

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = float('inf')

# O(N!)
for perm in permutations(range(N)):
    perm_cost = check_total_cost(perm)
    if perm_cost is None:
        continue
    answer = min(perm_cost, answer)
print(answer)