import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = []

for _ in range(N):
    houses.append(int(input()))
    
houses.sort()

# 제일 인접한 거리가 n 이상이 되도록 c개를 설치 가능?
def can_build(n):
    # 첫 집에는 무조건 설치
    loc = houses[0]
    total = 1               # 설치한 공유기 수
    min_dist = float('inf') # 가장 인접한 두 공유기 간 위치
    
    # 나머지 C - 1개 설치
    for i in range(1, len(houses)):
        if houses[i] - loc >= n:
            total += 1
            min_dist = min(min_dist, houses[i] - loc)
            loc = houses[i]
            if total == C:
                break

    if total == C:
        # C개를 다 설치한 경우, 제일 인접한 거리 반환
        return min_dist

    # C개를 다 설치하지 못한 경우, 좁혀야 함
    return False    
    
# 이분탐색
def binary_search():
    left = 1
    right = max(houses) - min(houses)

    while left <= right:
        n = (left + right) // 2
        
        result = can_build(n)
            
        # 설치 가능: 일단 설치하고, 더 넓힐 수 있나 확인
        if result:
            answer = result
            left = result + 1
            
        # 설치 부가능: 더 줄여야 함
        else:
            right = n - 1
            
    return answer

print(binary_search())