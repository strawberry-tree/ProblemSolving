from collections import deque
N = int(input())
queue = deque(map(int, input().split()))
stack = []

def check():
    for i in range(1, N + 1):
        while True:
            if queue and queue[0] == i:
                queue.popleft()
                break
            elif stack and stack[-1] == i:
                stack.pop()
                break
            elif queue:
                stack.append(queue.popleft())
            else:
                return False
    return True

if check():
    print("Nice")
else:
    print("Sad")