def solution(N, stages):
    users = [0] * (N + 2)         # 각 스테이지별 도달 사용자 수
    failure = [0] * (N + 1)       # 각 스테이지별 실패율
    
    # stages 배열 순회하면서 users 배열 업데이트
    for s in stages:
        for idx in range(1, s + 1):
            users[idx] += 1
    
    # users 배열 순회하면서 실패율 계산
    for idx in range(1, N + 1):
        # 도달 유저가 없는 경우
        if users[idx] == 0:
            failure[idx] = 0
        else:
            failure[idx] = (users[idx] - users[idx+1]) / users[idx]

    # 실패율 내림차순 기준으로 [1, 2, 3, .., N] 배열 정렬
    answer = list(range(1, N + 1))
    answer.sort(key=lambda x: (-failure[x], x))
    
    return answer
