from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for num_menu in course:
        cmb_list = []
        for order in orders:
            for cmb in combinations(order, num_menu):
                cmb_list.append(tuple(sorted(cmb)))
                
        if not cmb_list:
            continue
            
        cmb_counts = Counter(cmb_list)
        
        max_count = max(cmb_counts.values())
        
        if max_count < 2:
            continue

        for key, value in cmb_counts.items():
            if value == max_count:
                answer.append("".join(key))
        
    answer.sort()
    return answer
