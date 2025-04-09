# 문자열 회전 (O(N))
def rotate(s, num):
    return s[num:] + s[:num]

# 올바른 괄호 문자열? (O(N))
def check(s):
    # 괄호 문자열
    match = {"(": ")", "[": "]", "{": "}"}
    
    stack = []
    for letter in s:
        if letter in ["(", "[", "{"]:
            stack.append(letter)
        else:
            # 짝을 이룰 여는 괄호가 없는 경우
            if not stack:
                return False
            open = stack.pop()
            
            # 닫는 괄호와 여는 괄호가 쌍을 안 이루는 경우
            if match[open] != letter:
                return False
    
    # 짝을 찾지 못한 여는 괄호가 없어야 함
    if stack:
        return False
    else:
        return True
            
def solution(s):
    answer = 0
    
    # x칸씩 회전 반복 (O(N^2))
    for x in range(0, len(s)):
        result = check(rotate(s, x))
        if result:
            answer += 1
        
    return answer