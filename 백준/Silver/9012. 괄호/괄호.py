T = int(input())

def check_valid(string):
    count = 0
    
    for par in string:
            
        if par == "(":  # 여는 괄호
            count += 1
        else:           # 닫는 괄호
            if count <= 0:  # 짝을 이룰 열린 괄호가 없음
                return False
            count -= 1
    
    if count > 0:          # 짝을 못 찾은 열린 괄호가 남음
        return False
    return True

for _ in range(T):
    if check_valid(input()):
        print("YES")
    else:
        print("NO")