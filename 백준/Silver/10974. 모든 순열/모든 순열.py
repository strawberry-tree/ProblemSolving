from itertools import permutations
N = int(input())

for pm in permutations(range(1, N + 1)):
    print(*pm)
