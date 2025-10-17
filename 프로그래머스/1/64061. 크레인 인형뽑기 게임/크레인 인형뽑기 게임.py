def solution(board, moves):
    # 각 열을 스택으로 관리
    N = len(board)
    stacks = [[] for _ in range(N)]
    final_stack = []
    
    # j번째 열
    for j in range(N):
        # i번째 행, 스택이니까 역순
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                stacks[j].append(board[i][j])
        
    answer = 0
    # 인형뽑기
    for m in moves:
        if not stacks[m - 1]:
            continue
            
        doll = stacks[m - 1].pop()
        if final_stack and doll == final_stack[-1]:
            final_stack.pop()
            answer += 2
        else:
            final_stack.append(doll)
    
    return answer