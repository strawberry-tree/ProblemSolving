def get_total(string):
    stack = []
    total = 0
    
    for letter in string:
        if letter == "(" or letter == "[":
            stack.append([letter, 0])
        elif letter == ")":
            if stack and stack[-1][0] == "(": # 짝을 이룸
                pop_elem = stack.pop()
                if stack:
                    stack[-1][1] += 2 * max(1, pop_elem[1])
                else:
                    total += 2 * max(1, pop_elem[1])    
            else:   # 짝을 이루는 "("가 없음
                return 0
        elif letter == "]":
            if stack and stack[-1][0] == "[": # 짝을 이룸
                pop_elem = stack.pop()
                if stack:
                    stack[-1][1] += 3 * max(1, pop_elem[1])
                else:
                    total += 3 * max(1, pop_elem[1])
            else:
                return 0
    
    # 짝을 못 이룬 "(", "["가 남아 있음
    if len(stack) > 0:
        return 0
    else:
        return total

string = input()
print(get_total(string))