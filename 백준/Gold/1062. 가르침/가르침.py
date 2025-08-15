import sys
input = sys.stdin.readline

from itertools import combinations
N, K = map(int, input().rstrip().split())
words = []

for _ in range(N):
    words.append(set(input().rstrip()))

def get_answer(words, K):
    answer = 0
    
    if K < 5:
        return 0

    # 모든 가능 조합에 대해...
    for letters in combinations("bdefghjklmopqrsuvwxyz", K - 5):
        set_letters = set(letters) | {"a", "n", "t", "i", "c"}
        count = 0
        for word in words:
            if word <= set_letters:
                count += 1
        
        answer = max(answer, count)

    return answer

print(get_answer(words, K))    
    