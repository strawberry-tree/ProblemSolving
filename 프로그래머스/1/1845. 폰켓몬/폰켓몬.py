def solution(nums):
    n = len(nums)
    nums_set = set(nums)
    
    return min(n // 2, len(nums_set))