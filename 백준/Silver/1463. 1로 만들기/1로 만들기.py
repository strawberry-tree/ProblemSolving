from collections import deque

x = int(input())
memo = [None] * (x + 1)

queue = deque([1])
memo[1] = 0

def bfs():
    while queue:
        curr = queue.popleft()
        if curr == x:
            return memo[x]
        for num in [curr * 3, curr * 2, curr + 1]:
            if num <= x and memo[num] is None:              
                memo[num] = memo[curr] + 1
                queue.append(num)

print(bfs())