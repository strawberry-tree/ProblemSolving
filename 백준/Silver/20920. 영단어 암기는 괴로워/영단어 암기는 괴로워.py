from collections import Counter

N, M = map(int, input().split())
words = []

# 단어 리스트
for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    words.append(word)

# 단어의 수 세기
words_count = Counter(words)

# 중복 단어 제거
words = list(set(words))

# 정렬: 자주 나오는 순서 -> 단어의 길이 -> 알파벳 사전순
# 역순은 - 붙이기
words.sort(key=lambda x: (-words_count[x], -len(x), x))

for word in words:
    print(word)