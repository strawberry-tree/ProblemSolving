import bisect

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
for target in map(int, input().split()):
    result = bisect.bisect_right(cards, target) - bisect.bisect_left(cards, target)
    
    if result > 0:
        print(1, end=" ")
    else:
        print(0, end=" ")