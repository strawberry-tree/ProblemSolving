N, M = map(int, input().split())

mat_A = []
for _ in range(N):
    mat_A.append(list(map(int, input().split())))
    
M, K = map(int, input().split())
mat_B = []
for _ in range(M):
    mat_B.append(list(map(int, input().split())))
    
mat_C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        value = 0
        for k in range(M):
            value += mat_A[i][k] * mat_B[k][j]
        mat_C[i][j] = value

for i in range(N):
    print(*mat_C[i])