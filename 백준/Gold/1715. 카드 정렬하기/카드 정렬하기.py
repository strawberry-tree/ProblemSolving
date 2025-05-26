import sys
input = sys.stdin.readline
import heapq

N = int(input())
cards = []

# O(N)
for _ in range(N):
    cards.append(int(input()))

# 힙으로 바꿔주기 O(N)
heapq.heapify(cards)

curr = 0

while len(cards) >= 2:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    heapq.heappush(cards, card1 + card2)
    curr += card1 + card2
    
print(curr)