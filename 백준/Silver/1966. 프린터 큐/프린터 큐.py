def check():
    order = 0
    while queue:
        curr = queue.pop(0)
        for next in queue:
            if priority[curr] < priority[next]:
                queue.append(curr)
                break
        else:
            order += 1
            if curr == m:
                return order

num_cases = int(input())

for _ in range(num_cases):
    n, m = map(int, input().split())
    queue = [i for i in range(n)]
    priority = list(map(int, input().split()))
    print(check())