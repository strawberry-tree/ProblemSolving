N, K = map(int, input().split())
coins = []
answer = 0

for _ in range(N):
    coins.append(int(input()))
    
coins.sort(reverse=True)

for c in coins:
    answer += K // c
    K = K % c
    
print(answer)