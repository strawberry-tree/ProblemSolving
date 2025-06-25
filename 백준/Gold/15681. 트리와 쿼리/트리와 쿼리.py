import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
children = [[] for _ in range(N + 1)]   # 너의 자식들은 누구니
graph = [[] for _ in range(N + 1)]
size = [None] * (N + 1)

# 그래프 구성
for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)
    
    
def make_tree(node_x, parent):
    for node_y in graph[node_x]:
        if node_y != parent:
            children[node_x].append(node_y)
            make_tree(node_y, node_x)
            
def count_subtree_nodes(node_x):
    size[node_x] = 1
    for node_y in children[node_x]:
        count_subtree_nodes(node_y)
        size[node_x] += size[node_y]
        
make_tree(R, -1)
count_subtree_nodes(R)

# 쿼리의 답 출력
for _ in range(Q):
    U = int(input())
    print(size[U])