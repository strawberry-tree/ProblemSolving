from collections import Counter

def solution(N, stages):
    people_num = len(stages)    # 총 인원 수
    stages_counter = Counter(stages)    # {스테이지번호: 실패인원 수}
    failure_rate = {} # {스테이지번호: 실패율}
    
    for i in range(1, N + 1):
        if people_num == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = stages_counter[i] / people_num
            people_num -= stages_counter[i]
        
    answer = [i for i in range(1, N + 1)]
    answer.sort(key = lambda x: failure_rate[x], reverse=True)
    
    return answer