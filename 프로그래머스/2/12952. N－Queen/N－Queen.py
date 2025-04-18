def check(n, x, y, queens):
    for qx, qy in queens:
        if qx == x or qy == y:
            return False
        if abs(x - qx) == abs(y - qy):
            return False
    return True

def place(n, x, queens, answer):
    # x행에 퀸을 배치한다.
    # 모든 행에 퀸 배치가 완료된 경우
    if x >= n:
        return answer + 1
    
    # y열에 퀸을 배치할 수 있는지 확인
    for y in range(n):
        if check(n, x, y, queens):
            queens.add((x, y))
            answer = max(answer, place(n, x + 1, queens, answer))
            queens.remove((x, y))
    return answer

def solution(n):
    queens = set()
    answer = place(n, 0, queens, 0)
    return answer