N = int(input())
list_A = list(map(int, input().split()))

M = int(input())
list_B = list(map(int, input().split()))

DP = [[[] for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if list_A[i - 1] == list_B[j - 1]:
            temp = DP[i - 1][j - 1] + [list_A[i - 1]]
            while len(temp) >= 2:
                if temp[-2] < temp[-1]:
                    temp[-2] = temp[-1]
                    temp.pop()
                else:
                    break
                
            DP[i][j] = temp 
                
            
        else:
            left = DP[i - 1][j]
            right = DP[i][j - 1]
            idx = 0
            
            while idx < len(left) and idx < len(right):
                if left[idx] < right[idx]:
                    DP[i][j] = right[:]
                    break
                elif left[idx] > right[idx]:
                    DP[i][j] = left[:]
                    break
                else:
                    idx += 1
            else:
                if idx == len(left):
                    DP[i][j] = right[:]
                else:
                    DP[i][j] = left[:]
 
if not DP[-1][-1]:
    print(0)
else:
    print(len(DP[-1][-1]))                                     
    print(*DP[-1][-1])
        