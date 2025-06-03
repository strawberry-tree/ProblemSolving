from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

def dfs(K, coins):
    # K원을 만들 때 필요한 동전의 최소 개수
    # 확인하지 않은 경우 None
    answer = [None] * (K + 1)
    answer[0] = 0

    # 현재 금액, 동전 수
    queue = deque([0])

    while queue:
        now = queue.popleft()
        for c in coins:
            after = now + c
        
            # 아직 확인하지 않은 금액
            # after <= K: 금액을 넘으면 의미가 없음
            if after <= K and answer[after] is None:
                queue.append(after)
                answer[after] = answer[now] + 1
                
                if after == K:
                    return answer[after]
                
    return -1

print(dfs(K, coins))