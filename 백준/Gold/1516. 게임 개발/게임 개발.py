from collections import deque, defaultdict

N = int(input())
indegrees = [0] * (N + 1) # 건물별 먼저 이어야되는 건물 수
graph = defaultdict(list)
times = [0] * (N + 1)     # 건물별 소요시간
added_times = [0] * (N + 1) # 각 건물별 추가시간 계산 용도
queue = deque([])

for i in range(1, N + 1):               # i 는 건물번호
    nums = list(map(int, input().split()))
    times[i] = nums[0]
    for j in nums[1:-1]:
        graph[j].append(i)              # j -> i로 가는 화살표
        indegrees[i] += 1
    if indegrees[i] == 0:               # 먼저 지어야 하는 건물 없음
        queue.append(i)

while queue:
    curr = queue.popleft()
    for adj in graph[curr]:
        indegrees[adj] -= 1
        added_times[adj] = max(added_times[adj], times[curr])
        if indegrees[adj] == 0:
            queue.append(adj)
            times[adj] += added_times[adj]

for i in range(1, N + 1):
    print(times[i])