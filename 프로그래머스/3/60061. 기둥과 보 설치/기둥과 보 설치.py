def build(x, y, a, curr):
    # 기둥 설치 가능 여부 반환
    if a == 0:
        return (y == 0                      # 바닥 위
        or (x, y - 1, 0) in curr            # 아래에 기둥이 있음
        or (x, y, 1) in curr                # 아래에 보의 왼쪽 끝이 있음
        or (x - 1, y, 1) in curr)           # 아래에 보의 오른쪽 끝이 있음
    
    # 보 설치 가능 여부 반환
    if a == 1:
        return ((x, y - 1, 0) in curr              # 왼쪽 끝 아래에 기둥이 있음
        or (x + 1, y - 1, 0) in curr               # 오른쪽 끝 아래에 기둥이 있음
        or ((x - 1, y, 1) in curr and (x + 1, y, 1) in curr))
        # 양끝에 보가 연결되어 있음

def destroy(x, y, curr):
    # 없앤 후 기존 설치 보/기둥에 대해 규칙이 안 깨지는지 확인
    for x, y, a in curr:
        if not build(x, y, a, curr):
            return False
    return True

def solution(n, build_frame):
    curr = set()
    
    for x, y, a, b in build_frame:
        if b == 1:          # 설치
            if build(x, y, a, curr):
                curr.add((x, y, a))
        elif b == 0:        # 철거
            curr.remove((x, y, a))
            if not destroy(x, y, curr):
                curr.add((x, y, a))
    
    result = []
    for x, y, a in list(curr):
        result.append([x, y, a])
    result.sort()
    
    return result
