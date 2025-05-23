N = int(input())
A = list(map(int, input().split()))
A.sort()    # 정렬은 필수!!

M = int(input())
targets = list(map(int, input().split()))

# 이진 탐색
def find(target):
    l = 0
    r = N - 1
    
    while l <= r:
        m = (l + r) // 2

        if A[m] == target:
            return 1
        elif A[m] < target:
            l = m + 1
        else:
            r = m - 1
    
    return 0


for target in targets:
    print(find(target))