# 시간복잡도 - O(N)
def solution(s):
    stack = []
    
    # 각 문자를 순회 - O(N)
    for letter in s:
        if not stack or stack[-1] != letter:
            stack.append(letter)
        else:
            stack.pop()
    
    if stack:
        return 0
    else:
        return 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer