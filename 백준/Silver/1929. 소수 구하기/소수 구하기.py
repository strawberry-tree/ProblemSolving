def aristotle(max_num):
    # True: 소수 / False: 소수 아님
    nums = [True] * (max_num + 1)
    nums[1] = False
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if not nums[i]:
            continue
        
        j = i
        while i * j <= max_num:
            nums[i * j] = False
            j += 1
            
    return nums
            
m, n = map(int, input().split())
aristotle_list = aristotle(n)

for i in range(m, n + 1):
    if aristotle_list[i]:
        print(i)