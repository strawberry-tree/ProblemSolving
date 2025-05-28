N, times = map(int, input().split())

# 행렬 A, B 곱하기
def matmul(A, B):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):       
            # AB의 행렬곱 C의 i행 j열
            # A의 i행, B의 j열 모든 원소를 서로 곱하고 합
            value = 0
            for k in range(N):
                value += A[i][k] * B[k][j]
            result[i][j] = value % 1000
    return result

# 행렬 grid의 times 제곱
def power(grid, times):
    # 그냥 grid를 return하면 안 되는 이유: B = 1일 때 나머지처리 안됨
    if times == 1:
        return grid
    else:
        half = power(grid, times // 2)
        if times % 2 == 0:
            return matmul(half, half)
        else:
            return matmul(matmul(half, half), power(grid, 1))
        
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        grid[i][j] = grid[i][j] % 1000

answer = power(grid, times)
for i in range(N):
    print(*answer[i])