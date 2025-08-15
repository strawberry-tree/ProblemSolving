import math
from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
input_list = []
for _ in range(T):
    input_list.append(tuple(map(int, input().split())))

# 에라토스테네스의 체 만들기
prime_list = [True] * 10000
prime_list[0] = False
prime_list[1] = False

for i in range(2, int(math.sqrt(9999)) + 1):
    if prime_list[i]:
        j = i
        while i * j <= 9999:
            prime_list[i * j] = False
            j += 1
            
def bfs(start, end):
    queue = deque()
    visited = set()
    queue.append((start, 0))
    visited.add(start)
    
    while queue:
        curr, answer = queue.popleft()
        if curr == end:
            return answer
        
        c_list = []
        for div in [1000, 100, 10, 1]:
            c_list.append(curr // div)
            curr = curr % div
            

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                elif c_list[i] == j:
                    continue

                new_digits = c_list.copy()
                new_digits[i] = j
                new_number = 1000 * new_digits[0] + 100 * new_digits[1] + 10 * new_digits[2] + new_digits[3]
                
                if prime_list[new_number] and new_number not in visited:
                    visited.add(new_number)
                    queue.append((new_number, answer + 1))
                    
    return "IMPOSSIBLE"
    
                
for start, end in input_list:
    print(bfs(start, end))