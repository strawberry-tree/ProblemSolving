# N자리 숫자 중 K개 지우기
N, K = map(int, input().split())
number = input()

stack = []
count = 0   # 총 몇 개를 지웠는지

# O(N)
for digit in number:
    while stack and int(stack[-1]) < int(digit) and count < K:
        stack.pop()  
        count += 1
    stack.append(digit)
  
print("".join(stack[:N-K]))