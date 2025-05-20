N, M = map(int, input().split())

picked = [False] * (N + 1)
curr = []


def pick(i):
    if i > M:
        for c in curr:
            print(c, end=" ")
        print()
    else:
        for k in range(1, N + 1):
            if not picked[k]:
                picked[k] = True
                curr.append(k)
                pick(i + 1)
                curr.pop()
                picked[k] = False
        
pick(1)