import sys
sys.setrecursionlimit(10**6)

def div_and_merge(a, start, end, temp):
    global target
    if start < end:
        mid = (start + end) // 2
        
        left_result = div_and_merge(a, start, mid, temp) 
        if left_result is not None:
            return left_result
        
        right_result = div_and_merge(a, mid + 1, end, temp)
        if right_result is not None:
            return right_result
        
        i = start
        j = mid + 1
        k = 0
        
        while i <= mid and j <= end: 
            if a[i] <= a[j]:
                temp[k] = a[i]
                i += 1
            else:
                temp[k] = a[j]
                j += 1
            k += 1
            
        while i <= mid:
            temp[k] = a[i]
            i += 1
            k += 1
        
        while j <= end:
            temp[k] = a[j]
            j += 1
            k += 1
        
        for x in range(k):
            a[start + x] = temp[x]
            target -= 1
            if target == 0:
                return temp[x]
    
N, target = map(int, input().split())
A = list(map(int, input().split()))
temp = [0] * len(A)
answer = div_and_merge(A, 0, len(A) - 1, temp)

if answer is None:
    print(-1)
else:
    print(answer)