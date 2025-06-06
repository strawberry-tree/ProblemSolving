import sys
input = sys.stdin.readline

N = int(input())
times = []

for _ in range(N):
    s, e = map(int, input().split())
    times.append((s, e))

# 시작시간이 빠른 순 sort
times.sort()

total = 0   # 가능한 회의 수
curr_finish = times[0][1]     # 현재 회의가 끝나는 시간

for s, e in times[1:]:
    # 현재 회의가 끝남
    if s >= curr_finish:
        total += 1
        curr_finish = e
    # 현재 주목 중인 회의보다 일찍 끝남
    elif e < curr_finish:
        curr_finish = e

total += 1

print(total) 