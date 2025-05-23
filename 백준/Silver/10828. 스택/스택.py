import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command = input().strip()
    
    if command.startswith("push"):
        _, value = command.split()
        stack.append(int(value))
    
    elif command == "top":
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack[-1])
    
    elif command == "size":
        print(len(stack))
        
    elif command == "empty":
        print(int(len(stack) == 0))
        
    elif command == "pop":
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack.pop())