import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    ranks = []
    
    for _ in range(N):
        a, b = map(int, input().split())
        ranks.append((a, b))
        
    ranks.sort(key = lambda x: x[0])
    
    cutline = ranks[0][1]
    count = 1
    
    for i in range(1, N):
        if ranks[i][1] < cutline:
            count += 1
            cutline = ranks[i][1]
            
    print(count)