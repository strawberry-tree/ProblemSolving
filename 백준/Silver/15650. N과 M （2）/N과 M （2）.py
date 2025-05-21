from itertools import combinations

N, M = map(int, input().split())

for cmb in combinations(range(1, N+1), M):
    for num in cmb:
        print(num, end=" ")
    print()
