

def solution(n):
    # x행 y열에 배치 가능?
    def check(x, y, placements):
        # 동일 열에 배치된 경우
        if y in placements:
            return False
        
        # 동일 대각선에 배치된 경우
        for i, j in enumerate(placements):
            if i + j == x + y or i - j == x - y:
                return False
        
        return True
            
    # x행에 채우기
    def fill_in(x):
        # 모두 채운 경우, 1가지 경우의 수
        if x >= n:
            return 1
        
        results = 0
        
        # 0 -> n - 1 열까지 시도
        for y in range(n):
            if check(x, y, placements):
                placements.append(y)
                results += fill_in(x + 1)
                placements.pop()
            
        return results
            
    # 0행부터 차례로 채우기
    placements = []
    return fill_in(0)