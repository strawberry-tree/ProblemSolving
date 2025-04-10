import math

def solution(progresses, speeds):
    
    finish = []
    result = []
    
    # 작업별 걸리는 날짜 계산, O(N)
    for i in range(len(progresses)):
        time = math.ceil((100 - progresses[i]) / speeds[i])
        
        # 앞 작업보다 짧게 걸림 -> 앞 작업과 동시에 끝남
        if finish and time <= finish[-1] :
            result[-1] += 1
            
        # 앞 작업보다 길게 걸림 -> 앞 작업보다 늦게 끝남
        # OR 첫 번째 작업일 때
        else:
            finish.append(time)
            result.append(1)
            
    return result