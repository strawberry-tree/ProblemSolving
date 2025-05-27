import sys
input = sys.stdin.readline

# 사대의 수, 동물의 수, 사정거리
M, N, L = map(int, input().split())

# 사대의 위치
sadaes = set(map(int, input().split()))

# 동물의 위치
dongmuls = []
for _ in range(N):
    dongmuls.append(list(map(int, input().split())))
    
# 지금 위치일 때, x마리 이상 사냥 가능?
# def can_fire(x):
    
count = 0
for x, y in dongmuls:
    sadae_left = max(min(sadaes), x - (L - y))
    sadae_right = min(max(sadaes), x + (L - y))
    can_fire_sadae = set(range(sadae_left, sadae_right + 1))
    if len(can_fire_sadae & sadaes) > 0:
        count += 1
        
print(count)
    
    