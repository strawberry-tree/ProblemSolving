N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

# 현재 합이 curr인 부분수열에 원소를 추가한다
# 단 인덱스 i 이후 원소만 추가할 수 있다
def check_sum(i, curr):
    # 더 추가할 원소가 없음
    if i >= N:
        if curr == S:
            return 1
        else:
            return 0

    count = 0
    
    # 더 추가 안 하고 멈추는 경우
    if i > 0:   # 빈 수열은 부분수열이 아님
        count += check_sum(N, curr)
    
    # 더 추가하는 경우
    for j in range(i, N):    
        count += check_sum(j + 1, curr + nums[j])
    
    return count 
    
print(check_sum(0, 0))