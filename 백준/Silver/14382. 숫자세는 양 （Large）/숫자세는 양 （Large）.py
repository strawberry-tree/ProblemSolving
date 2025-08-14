T = int(input())

def get_answer(N):
    if N == 0:
        return "INSOMNIA"
    curr_N = N
    nums = set(map(str, range(0, 10)))   # 0부터 9까지. 모든 수가 적히면 잠에 든다.
    while True:
        nums -= set(str(curr_N))
        if not nums:
            return curr_N
        curr_N += N
        
        
for i in range(T):
    print(f"Case #{i + 1}: {get_answer(int(input()))}")