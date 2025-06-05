# 물품수, 최대무게
N, K = map(int, input().split())
memo = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K - w, -1, -1):
        memo[i + w] = max(memo[i + w], memo[i] + v)
        
print(memo[-1])