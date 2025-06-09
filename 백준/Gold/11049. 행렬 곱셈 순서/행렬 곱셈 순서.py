import sys
input = sys.stdin.readline

N = int(input())
sizes = [tuple(map(int, input().split())) for _ in range(N)]

memo = [[0] * (N) for _ in range(N)]

def find_answer():
    for gap in range(1, N):
        for i in range(N - gap):
            j = i + gap
            temp = float('inf')
            
            for k in range(i, j):
                cost = memo[i][k] + memo[k + 1][j] + sizes[i][0] * sizes[k][1] * sizes[j][1]
                
                if cost < temp:
                    temp = cost
            
            if i == 0 and j == (N - 1):
                return temp
            memo[i][j] = temp
                
print(find_answer())