def solution(s):
    # 올바른 괄호 문자열?
    def check_correct(rotated_s):
        stack = []
        for letter in rotated_s:
            if letter == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif letter == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif letter == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif letter in ["{", "[", "("]:
                stack.append(letter)
            else:
                return False
        
        if (not stack):
            return True
        else:
            return False
                
    answer = 0
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]
        if check_correct(rotated_s):
            answer += 1
            
    return answer