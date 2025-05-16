C = int(input())

for _ in range(C):
    input_list = list(map(int, input().split()))
    N = input_list[0]
    scores = input_list[1:]
    mean_score = sum(scores) / N
    count = 0
    
    for i in range(N):
        if scores[i] > mean_score:
            count += 1
            
    print(f"{count / N * 100:.3f}%")
    