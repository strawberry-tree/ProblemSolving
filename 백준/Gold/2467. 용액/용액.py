N = int(input())
liquid = list(map(int, input().split()))

i = 0
j = N - 1
curr = float('inf')

while i < j:
    total = liquid[i] + liquid[j]
    if abs(total) < curr:
        curr = abs(total)
        left, right = i, j
        
    if total < 0:
        i += 1    
    else:
        j -= 1
            
print(liquid[left], liquid[right])