N = int(input())

x_list = []
y_list = []
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    
for i in range(N - 1):
    answer += x_list[i] * y_list[i + 1]
    answer -= x_list[i + 1] * y_list[i]

answer += x_list[N - 1] * y_list[0]
answer -= x_list[0] * y_list[N - 1]

answer = abs(answer) / 2

print(round(answer, 1))