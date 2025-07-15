def solution(n, lost, reserve):
    fail = 0                                            # 체육복이 없는 사람 수
    reserve_set = set(reserve) - set(lost)              # 여벌 체육복을 가져온 학생이, 체육복을 도난당했을 수 있음
    lost = list(set(lost) - set(reserve))
    lost.sort()
    
    # lost를 순회 -> 체육복을 빌려줄 사람이 존재하나?
    for l in lost:
        # 앞사람에게 빌릴 수 있나
        # lost를 정렬한 상태이므로, 앞사람부터 확인하는 게 맞음 (??)
        if (l - 1) in reserve_set:
            reserve_set.remove(l - 1)
        # 뒷사람에게 빌릴 수 있나
        elif (l + 1) in reserve_set:
            reserve_set.remove(l + 1)
        else:
            fail += 1
    return n - fail