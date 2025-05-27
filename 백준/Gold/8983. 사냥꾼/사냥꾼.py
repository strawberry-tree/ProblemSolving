import sys
input = sys.stdin.readline

# 사대의 수, 동물의 수, 사정거리
M, N, L = map(int, input().split())

# 사대의 위치
sadaes = list(map(int, input().split()))
sadaes.sort()

# 이분탐색: 쏠 수 있는 사대가 있나요?
def binary_search(fire_a, fire_b): 
    l = 0
    r = M - 1
    
    while l <= r:
        m = (l + r) // 2
        if fire_a <= sadaes[m] <= fire_b:
            return True
        elif sadaes[m] < fire_a:
            l = m + 1
        else:   # fire_b < sadaes[m]
            r = m - 1
    return False

# 동물 수 세기
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    fire_a = max(sadaes[0], x - (L - y))
    fire_b = min(sadaes[-1], x + (L - y))
    
    # 사대의 위치를 이분탐색으로?
    if binary_search(fire_a, fire_b):
        count += 1
        
print(count)