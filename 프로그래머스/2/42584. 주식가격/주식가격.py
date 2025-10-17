def solution(prices):
    # 현재 시점을 스택에 저장
    stack = []
    result = [0] * len(prices)
    
    # i: 현재시점
    for i in range(len(prices)):
    
        # 가격이 떨어진 경우 (stack[-1][0] -> 최근가격, stack[-1][1] -> 최근시점)
        while stack and prices[stack[-1]] > prices[i]:
            result[stack[-1]] = i - stack[-1]
            stack.pop()
            
        stack.append(i)
        
    # 끝까지 가격이 떨어지지 않은 경우
    for t in stack:
        result[t] = len(prices) - t - 1
        
    return result