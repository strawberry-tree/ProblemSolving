import sys
input = sys.stdin.readline

# 사대의 수, 동물의 수, 사정거리
M, N, L = map(int, input().split())

# 사대의 위치
sadaes = set(map(int, input().split()))
    
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    sadae_left = max(min(sadaes), x - (L - y))
    sadae_right = min(max(sadaes), x + (L - y))
    
    for s in sadaes:
        if sadae_left <= s <= sadae_right:
            count += 1
            break
        
print(count)
    
    