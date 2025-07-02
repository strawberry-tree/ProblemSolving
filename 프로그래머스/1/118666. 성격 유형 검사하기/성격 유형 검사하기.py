def solution(survey, choices):
    # 각 유형별 점수
    points = {key: 0 for key in "RTCFJMAN"}
    
    # 점수 채점
    for i in range(len(survey)):
        left_i = survey[i][0]       # 비동의 시 점수가 오르는 유형
        right_i = survey[i][1]      # 동의 시 점수가 오르는 유형
        ch = choices[i]             # 사용자의 응답

        if ch <= 3:                 # 비동의 선택지
            points[left_i] += (4 - ch)
        elif ch >= 5:               # 동의 선택 시
            points[right_i] += (ch - 4)
        
        
    # 유형 확인
    answer = []
    answer.append("R" if points["R"] >= points["T"] else "T")
    answer.append("C" if points["C"] >= points["F"] else "F")
    answer.append("J" if points["J"] >= points["M"] else "M")
    answer.append("A" if points["A"] >= points["N"] else "N")
    return "".join(answer)