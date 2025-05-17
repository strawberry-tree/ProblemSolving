N = int(input())

# num개의 원판을 A에서 B 위치로 옮김
def hanoi_moves(num, A, B):
    count = 0
    if num >= 1:
        # 바닥 원판 제외한 num-1개 원판을 A에서 중간 위치로 옮김
        count += hanoi_moves(num - 1, A, 6 - A - B)
        # 바닥 원판을 A에서 B로 옮김
        moves.append((A, B))
        count += 1
        # 바닥 원판 제외한 num-1개 원판을 중간 위치에서 B로 옮김
        count += hanoi_moves(num - 1, 6 - A - B, B)
    return count

def hanoi(num, A, B):
    if num in memo:
        return memo[num]
    count = 0
    if num >= 1:
        # 바닥 원판 제외한 num-1개 원판을 A에서 중간 위치로 옮김
        count += hanoi(num - 1, A, 6 - A - B)
        # 바닥 원판을 A에서 B로 옮김
        count += 1
        # 바닥 원판 제외한 num-1개 원판을 중간 위치에서 B로 옮김
        count += hanoi(num - 1, 6 - A - B, B)
        memo[num] = count
    return count

if N <= 20:
    moves = []
    print(hanoi_moves(N, 1, 3))
    for (a, b) in moves:
        print(a, b)
else:
    memo = dict()
    print(hanoi(N, 1, 3))