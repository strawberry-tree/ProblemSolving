width, height = map(int, input().split())
N = int(input())

garo_cuts = [0, height]
sero_cuts = [0, width]

for _ in range(N):
    cut, where = map(int, input().split())
    if cut == 0:
        garo_cuts.append(where)
    elif cut == 1:
        sero_cuts.append(where)

garo_cuts.sort()
sero_cuts.sort()

garo_lengths = []
sero_lengths = []

for i in range(len(garo_cuts) - 1):
    garo_lengths.append(garo_cuts[i + 1] - garo_cuts[i])
    
for i in range(len(sero_cuts) - 1):
    sero_lengths.append(sero_cuts[i + 1] - sero_cuts[i])
    
print(max(garo_lengths) * max(sero_lengths))
