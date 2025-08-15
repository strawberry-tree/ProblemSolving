import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

def check(left, right, result):    
    max_len = (left + right) // 2
    new_lines = 0

    for l in lines:
        new_lines += l // max_len

    if left > right:
        return result

    # 부족 -> 최대 길이를 줄여야 함
    if new_lines < n:
        return check(left, max_len - 1, result)

    # 이상 -> 최대 길이를 더 늘릴 수 있나?
    if new_lines >= n:
        result = max_len
        return check(max_len + 1, right, result)

print(check(1, max(lines), 1))