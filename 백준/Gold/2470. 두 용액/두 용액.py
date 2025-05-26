N = int(input())
values = list(map(int, input().split()))
values.sort()

left = 0
right = N - 1

answer_val = float('inf') # 특성값의 절댓값

while left < right:
    result = (values[left] + values[right])
    if abs(result) < answer_val:
        answer_val = abs(result)
        answer = (left, right)
        
    if result == 0:
        break
    elif result > 0:
        # 양의 값 -> 높은쪽 용액을 한 단계 낮은 걸로 교체
        right -= 1
    else:
        # 음의 값 -> 낮은쪽 용액을 한 단계 높은 걸로 교체
        left += 1
    
# 근데 이건 이분탐색이 아니라 투포인터 아닌가 음
# O(N)이긴 한데
print(values[answer[0]], values[answer[1]])
