def solution(strings, n):
    # 시간 복잡도 - O(N log N)
    strings.sort(key= lambda s: (s[n], s))
    return strings