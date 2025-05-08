from collections import defaultdict

def solution(topping):
    answer = 0
    
    before = defaultdict(int)
    after = defaultdict(int)
    before_set = set()
    after_set = set(topping)
    
    # O(N)
    for t in topping:
        after[t] += 1
    
    # 토핑을 1개씩 after에서 before로 넘기기
    # 일치할 시 answer에 1 추가
    # O(N)
    for t in topping:
        after[t] -= 1
        if after[t] == 0:
            after_set.remove(t)
        if before[t] == 0:
            before_set.add(t)
        before[t] += 1
        
        if len(before_set) == len(after_set):
            answer += 1
    return answer