def solution(board, moves):
    N = len(board)
    
    stacks = [[] for _ in range(N)] # 뽑기 전 인형들의 스택의 리스트 
    final_stack = []                # 뽑은 인형들의 스택
    result = 0                      # 터뜨린 인형 수
    
    # 각 스택에 인형을 넣어줌 - O(N^2)
    for col in range(N):
        for row in range(N - 1, -1, -1):
            doll = board[row][col]
            if doll != 0:
                stacks[col].append(doll)
    
    # 인형을 뽑고 최종 스택에 넣기 - O(M)
    for m in moves:
        m -= 1
        if stacks[m]:
            doll = stacks[m].pop()
        else:
            continue
            
        # 최상단 인형이랑 동일한 경우 pop, 아니면 push
        if final_stack and final_stack[-1] == doll:
            final_stack.pop()
            result += 2
        else:
            final_stack.append(doll)
    
    return result