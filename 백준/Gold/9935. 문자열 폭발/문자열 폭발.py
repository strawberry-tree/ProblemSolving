string = input()    # 입력한 문자열
target = list(input())    # 폭발 문자열

stack = []

def check(stack, target):
    N = len(target)
    
    # 스택 최상단에 폭발 문자열 존재하면, 계속 팝 
    while stack[-N:] == target:
        for _ in range(N):
            stack.pop()

for letter in string:
    stack.append(letter)
    check(stack, target)

if not stack:               # 남은 문자가 없음
    print("FRULA")
else:                       # 남은 문자열을 출력
    print("".join(stack))