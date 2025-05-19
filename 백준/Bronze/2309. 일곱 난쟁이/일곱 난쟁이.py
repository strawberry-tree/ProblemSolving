def find_fake(heights):
    for i in range(9):      # i: 첫번째 가짜 난쟁이
        for j in range(i + 1, 9):  # j: 두번째 가짜 난쟁이
            total = 0
            # i번째, j번째 난쟁이 빼고 합을 구함
            for k in range(9):
                if i == k or j == k:
                    continue
                total += heights[k]
            if total == 100:
                return i, j

heights = []
for i in range(9):
    heights.append(int(input()))

fake1, fake2 = find_fake(heights)

answer = []

for i in range(9):
    if i != fake1 and i != fake2:
        answer.append(heights[i])
        
answer.sort()

for a in answer:
    print(a)
            