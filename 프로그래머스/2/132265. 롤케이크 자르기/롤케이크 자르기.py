from collections import defaultdict
from collections import Counter

def solution(topping):
    answer = 0
    
    after_dict = Counter(topping)
    before_set = set()
    
    # 토핑을 1개씩 after_dict에서 before_set로 넘기기
    # 먹을 수 있는 토핑 수가 일치할 시 answer에 1 추가
    # O(N)
    for t in topping:
        after_dict[t] -= 1
        if after_dict[t] == 0:
            after_dict.pop(t)
        before_set.add(t)
        if len(before_set) == len(after_dict):
            answer += 1
    return answer