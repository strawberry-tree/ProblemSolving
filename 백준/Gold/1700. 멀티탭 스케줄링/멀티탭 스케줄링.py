from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tools = list(map(int, input().split()))
plugs = set()
locs = dict()
count = 0

for i in range(K):
    if tools[i] not in locs:
        locs[tools[i]] = deque()
    locs[tools[i]].append(i)

for i in range(K):
    
    # 플러그가 꽉 찼는데 새로운 앨 넣어야 해??
    # 그럼 하날 빼야즤~~~~ 하하호호~~~
    if len(plugs) == N and tools[i] not in plugs:
        jail_mun_loc = -1
        for p in plugs:
            # 더 이상 쓸 일이 없는 경우
            if not locs[p]:
                jail_mun_idx = p
                break
            elif locs[p][0] > jail_mun_loc:
                jail_mun_idx = p
                jail_mun_loc = locs[p][0]
                
        plugs.remove(jail_mun_idx)
        count += 1
        
    plugs.add(tools[i])
    locs[tools[i]].popleft()
    
print(count)

