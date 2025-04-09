def get_position(n, idx):
    # 1차원 배열 좌표 -> 2차원 배열 좌표
    return idx // n, idx % n

def get_value(x, y):
    return max(x, y) + 1

def solution(n, left, right):
    answer = []
    # 2차원 배열에서의 해당 값 구하기
    for idx in range(left, right + 1):
        answer.append(get_value(*get_position(n, idx)))
    return answer
    