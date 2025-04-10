def solution(s):
    # "바로 전에 더했던 숫자" -> 스택
    stack = []
    
    # s.split()의 길이가 N일 때, O(N)
    for letter in s.split():
        if letter == "Z":
            stack.pop()
        else:
            stack.append(int(letter))

    # 각 원소의 합, O(N)
    return sum(stack)