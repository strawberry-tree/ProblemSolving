def find(x, parent):
    if parent[x] != x: 
        parent[x] = find(parent[x], parent) # 경로압축
    return parent[x]

def union(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_x] = root_y
            rank[root_y] += 1
        return True
    else:
        # 이미 부모 노드가 동일, 안 지어도 됨
        return False        

def solution(n, costs):
    parent = list(range(n))    # 부모노드
    rank = [0] * n      # 랭크
    total = 0           # 전체 비용
    
    # 저렴한 순서대로 sort
    costs.sort(key = lambda x: x[2])
    
    # 부모 노드가 다른 경우 연결, 같은 경우 생략
    for cx, cy, cost in costs:
        if union(cx, cy, parent, rank):
            total += cost
    
    return total