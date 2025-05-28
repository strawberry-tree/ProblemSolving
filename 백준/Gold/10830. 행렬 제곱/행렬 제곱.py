# import sys
# input = lambda: sys.stdin.readline().rstrip()

N, B = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

dp = dict()

def matmul(X, Y):
    Z = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            result = 0
            for k in range(N):
                result += X[i][k] * Y[k][j]
            Z[i][j] = result % 1000

    return Z

def matpower(A, B):
    if B not in dp:
        if B == 1:
            dp[B] = A
        elif B % 2 == 0:
            C = matpower(A, B // 2)
            dp[B] = matmul(C, C)
        else:
            C = matpower(A, B // 2)
            D = matpower(A, B // 2 + 1)
            dp[B] = matmul(C, D)
    return dp[B]


result = matpower(A, B)
for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=" ")
    print()