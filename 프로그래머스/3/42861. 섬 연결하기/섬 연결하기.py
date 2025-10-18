def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)
    
    if root_x == root_y:
        return False
    else:
        parent[root_x] = root_y
        return True

def solution(n, costs):
    # 비용 오름차순으로 정렬
    costs.sort(key=lambda x:x[2])
    answer = 0
    parent = [i for i in range(n)]
    
    # 섬1, 섬2, 비용
    for i1, i2, cost in costs:
        if union(i1, i2, parent):
            answer += cost
    
    return answer