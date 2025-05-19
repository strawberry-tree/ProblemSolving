from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(input()))

def find_comb(heights):
    for comb in combinations(heights, 7):
        if sum(comb) == 100:
            return list(comb)
        
answer = find_comb(heights)
answer.sort()

for a in answer:
    print(a)