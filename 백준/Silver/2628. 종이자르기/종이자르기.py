A, B = map(int, input().split()) # A: 가로의 길이, B: 세로의 길이
T = int(input())

a_cuts = [0, A]
b_cuts = [0, B]

for _ in range(T):
    how, loc = map(int, input().split())
    if how == 0:    # 가로 자르기
        b_cuts.append(loc)
    elif how == 1:  # 세로 자르기
        a_cuts.append(loc)
        
a_cuts.sort()
b_cuts.sort()

a_lens = []
b_lens = []    

for i in range(1, len(a_cuts)):
    a_lens.append(a_cuts[i] - a_cuts[i-1])

for i in range(1, len(b_cuts)):
    b_lens.append(b_cuts[i] - b_cuts[i-1])

result = max(a_lens) * max(b_lens)
print(result)