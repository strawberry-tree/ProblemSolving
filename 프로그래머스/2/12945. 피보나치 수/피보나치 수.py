def solution(n):
    nums = [0] * (n + 1)
    nums[0] = 0
    nums[1] = 1
    
    for i in range(2, n + 1):
        nums[i] = (nums[i - 1] + nums[i - 2]) % 1234567
    return nums[n]