from collections import deque

N = int(input())
balloons = list(map(int, input().split()))
queue = deque()

for idx, num in enumerate(balloons):
    # 풍선 번호 및 적힌 숫자
    queue.append((idx + 1, num))

while queue:
    popped, move = queue.popleft()
    print(popped, end=" ")
    if move > 0:
        queue.rotate(-1 * move + 1)
    else:    
        queue.rotate(-1 * move)