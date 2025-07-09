H, W = map(int, input().split())
heights = list(map(int, input().split()))

# 높이별 블록의 존재 위치
# blocks[i]: i층에서 블록의 존재 위치

blocks = [[] for _ in range(H + 1)]
for j in range(len(heights)):
    for i in range(1, heights[j] + 1):
        blocks[i].append(j)

# 고이는 빗물의 총량 계산
answer = 0
for i in range(1, H + 1):
    for j in range(1, len(blocks[i])):
        answer += (blocks[i][j] - blocks[i][j - 1] - 1)
    
print(answer)