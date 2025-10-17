def solution(s):
    stack = []
    
    for letter in s:
        if stack and letter == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
        
    if stack:
        return 0
    else:
        return 1