from collections import deque

N = int(input())
deck = deque(range(1, N + 1))

while len(deck) > 1:
    # 맨 위 버리기
    deck.popleft()
    
    # 아래로 옮기기
    deck.append(deck.popleft())
    
print(deck[0])