import heapq

N = int(input())
lectures = []

for _ in range(N):
    num, start, end = map(int, input().split())
    lectures.append((num, start, end))
    
lectures.sort(key=lambda x: (x[1], x[2], x[0]))

queue = []
answer = dict()
num_rooms = 0

for num, start, end in lectures:
    if queue and start >= queue[0][0]:
        _, room_no = heapq.heappop(queue)
        heapq.heappush(queue, (end, room_no))
        answer[num] = room_no
    else:
        num_rooms += 1
        heapq.heappush(queue, (end, num_rooms))
        answer[num] = num_rooms
        
print(num_rooms)
for i in range(1, N + 1):
    print(answer[i])