

def solution(n, info):
    # 점수 정산
    def calc_points(scores):
        tally = {"ryan": 0, "apeach": 0}
        for i in range(10):
            points = 10 - i
            apeach = info[i]    # 어피치가 쏜 화살 수
            ryan = scores[i]

            if ryan > apeach:
                tally["ryan"] += points
            elif ryan == 0 and apeach == 0:
                pass
            else:
                tally["apeach"] += points

        return (tally["ryan"] - tally["apeach"], scores.copy())
    
    # target점에 쏠 수 있음 / arrows개 화살 남음 / 현재 총점 total
    def fire(target, arrows):
        
        # 모두 다 쐈거나 화살이 떨어진 경우
        if target >= 10:
            scores[0] = arrows
            result = calc_points(scores)
            scores[0] = 0
            return result
        
        if arrows <= 0:
            return calc_points(scores)
        
        max_diff, answer = 0, None
        
        # 이번에 hits개 쏠 때
        for hits in range(0, arrows + 1):
            scores[10 - target] = hits
            diff, hits_list = fire(target + 1, arrows - hits)
            if max_diff <= diff:
                max_diff, answer = diff, hits_list
            scores[10 - target] = 0
        
        return max_diff, answer
            
    scores = [0] * 11   # 10점 -> 0점 순, 0점은 생략
    diff, answer = fire(0, n)   # 0점부터 쏘기
    if diff <= 0:
        return [-1]
    return answer