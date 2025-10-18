def solution(n,a,b):
    
    i = 1   # 1라운드부터 시작
    
    while True:
        a_team = (a - 1) // (2 ** i)
        b_team = (b - 1) // (2 ** i)
    
        if a_team == b_team:
            return i
        i += 1