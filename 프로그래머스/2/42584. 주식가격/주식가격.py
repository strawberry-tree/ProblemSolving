def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    # prices 순회 - O(N)
    for idx, p in enumerate(prices):
        # 값이 떨어지는 상황
        while stack and stack[-1][1] > p:
            d_idx, d_p = stack.pop()
            # (값이 떨어진 시점 - 원래 시점)
            answer[d_idx] = idx - d_idx
        else:
            # 제일 최근의 시점을 (현재 시점, 현재 가격)으로 저장
            stack.append((idx, p))
    
    # 값이 떨어지지 않은 경우도 처리 - O(N)
    while stack:
        d_idx, d_p = stack.pop()
        answer[d_idx] = idx - d_idx
    
    return answer