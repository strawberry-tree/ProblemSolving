# 시간복잡도 - O(N)
def solution(s):
    stack = []

    # 각 문자를 순회 - O(N)
    for letter in s:
        if not stack or stack[-1] != letter:
            stack.append(letter)
        else:
            stack.pop()

    return int(not stack)
