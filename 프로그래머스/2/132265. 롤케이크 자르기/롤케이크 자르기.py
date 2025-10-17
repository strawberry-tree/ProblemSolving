from collections import Counter
def solution(topping):    
    # 자를 수 있는 경우의수: idx(0) -> (1) 사이 -> idx (n-2)->(n-1) 사이
    answer = 0
    first_piece = Counter(topping)
    second_piece = set()
    
    for t in topping:
        first_piece[t] -= 1 # 첫째 조각
        if first_piece[t] == 0:
            del first_piece[t]
        second_piece.add(t) # 둘째 조각
        
        if len(first_piece) == len(second_piece):
            answer += 1
        
    return answer