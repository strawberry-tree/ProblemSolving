N = int(input())
heights = list(map(int, input().split()))
stack = []
answer = [0] * (N + 1)

for i in range(len(heights), 0, -1):
    height = heights[i - 1]
    while stack and stack[-1][1] <= height:
        answer[stack.pop()[0]] = i
        
    stack.append((i, heights[i - 1]))   # 탑 번호, 탑 높이
    
print(*(answer[1:]))