import sys
input = sys.stdin.readline
N = int(input())

# 1 실내 0 실외
in_out = [0] + list(map(int, input().strip()))
graph = [[] for _ in range(N + 1)]
count = 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)

def dfs(i, curr):
    global count
    
    # 실내인 경우
    if in_out[i] == 1:
        count += 2 * len(curr)
        for j in graph[i]:
            dfs(j, {i})
        curr.add(i)
        return curr 

    # 실외인 경우
    else:
        for j in graph[i]:
            curr = dfs(j, curr)
        

dfs(1, set())
print(count)