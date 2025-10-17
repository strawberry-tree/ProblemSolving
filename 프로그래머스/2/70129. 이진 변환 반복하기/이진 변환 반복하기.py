def solution(s):
    
    def change(x):
        removed_zeros = 0
        
        # 1. 모든 0을 제거합니다
        x_list = [i for i in list(x) if i == "1"]
        removed_zeros = len(x) - len(x_list)
    
        # 2. 길이 c를 2진법으로 표현한 문자열로 바꿉니다
        c = len(x_list)
        
        # 현재 값, 제거된 0의 개수
        changed_x = bin(c)[2:]
        return (changed_x, removed_zeros)
    
    change_total = 0
    zero_total = 0
    while s != "1":
        s, removed_zeros = change(s)
        change_total += 1
        zero_total += removed_zeros
    
    return [change_total, zero_total]