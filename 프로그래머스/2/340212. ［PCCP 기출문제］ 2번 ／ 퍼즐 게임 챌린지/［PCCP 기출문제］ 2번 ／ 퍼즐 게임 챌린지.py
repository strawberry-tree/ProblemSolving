def check_time(level, diffs, times):
    N = len(diffs)
    total_time = 0
    
    for i in range(N):
        
        # 정보
        diff = diffs[i]
        time_cur = times[i]
    
        if i >= 1:
            time_prev = times[i - 1]
        else:
            time_prev = 0
        
        # 시간계산
        if diff <= level:
            total_time += time_cur
        else:
            total_time += ((time_cur + time_prev) * (diff - level) + time_cur)
        
    return total_time

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    while left <= right:
        mid = (left + right) // 2
        total_time = check_time(mid, diffs, times)
        
        # 제한시간 통과
        if total_time <= limit:
            answer = mid
            right = mid - 1
            
        # 제한시간 통과 실패
        else:
            left = mid + 1
        
    return answer