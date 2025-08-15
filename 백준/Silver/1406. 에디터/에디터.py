import sys
from collections import deque

input = sys.stdin.readline

queue = deque(input().rstrip())
commands = int(input())
location = len(queue)
rotated = 0

for _ in range(commands):
    c_list = input().rstrip().split()
    if c_list[0] == "P":
        # 커서 왼쪽에 문자 추가
        queue.append(c_list[1])
        location += 1
    elif c_list[0] == "L":
        # 커서를 왼쪽으로 한 칸 옮김  (문장 맨 앞이면 무시)
        if location > 0:
            queue.rotate(1)
            location -= 1
    elif c_list[0] == "D":
        # 커서를 오른쪽으로 한 칸 옮김  (문장 맨 뒤면 무시)
        if location < len(queue):
            queue.rotate(-1)
            location += 1
    elif c_list[0] == "B":
        # 커서 왼쪽의 문자를 삭제 (문장 맨 앞이면 무시)
        if location > 0:
            queue.pop()
            location -= 1
        
queue.rotate(location)
print("".join(queue))