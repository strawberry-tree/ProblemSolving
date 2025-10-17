from collections import Counter
def solution(k, tangerine):
    t_count = Counter(tangerine)
    total = 0   # 몇 개
    answer = 0  # 몇 종류
    
    values = list(t_count.values())
    values.sort(reverse=True)
    # 많은 애들부터...
    for v in values:
        total += v
        answer += 1
        if total >= k:
            break
            
    return answer