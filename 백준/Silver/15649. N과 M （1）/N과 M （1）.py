import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())

chosen = [False] * (N + 1)

def perm(curr, chosen):
    if len(curr) >= M:
        print(*curr)
        return
    
    for i in range(1, N + 1):
        if not chosen[i]:
            chosen[i] = True
            curr.append(i)
            perm(curr, chosen)
            curr.pop()
            chosen[i] = False
            
perm([], chosen)