def solution(s):
    stack = []
    
    for letter in s:
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if not stack:
                return False
            stack.pop()
    
    return not(stack)