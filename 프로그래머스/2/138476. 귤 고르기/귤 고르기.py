from collections import Counter

def solution(k, tangerine):
    result = 0
    counts = Counter(tangerine)
    for _, c in counts.most_common():
        k -= c
        result += 1
        if k <= 0:
            break
    return result