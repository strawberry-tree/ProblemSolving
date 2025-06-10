N = int(input())
A = list(map(int, input().split()))
dp_inc = [0] * N
dp_dec = [0] * N

for i in range(N):
    dp_inc[i] = 1
    max_prev = 0
    for j in range(i):
        if A[j] < A[i]:
            max_prev = max(max_prev, dp_inc[j])
    dp_inc[i] += max_prev
    
for i in range(N - 1, -1, -1):
    dp_dec[i] = 1
    max_prev = 0
    for j in range(i + 1, N):
        if A[j] < A[i]:
            max_prev = max(max_prev, dp_dec[j])
    dp_dec[i] += max_prev

results = []
for i in range(N):
    results.append(dp_inc[i] + dp_dec[i] - 1)
    
print(max(results))