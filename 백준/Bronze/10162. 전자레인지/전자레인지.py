T = int(input())

answer = [0, 0, 0]
times = [300, 60, 10]
for i in range(3):
    answer[i] = T // times[i]
    T = T % times[i]
    
if T != 0:
    print(-1)
else:
    print(*answer)
    