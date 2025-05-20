n = int(input())
nums = list(map(int, input().split()))
plus, minus, times, div = map(int, input().split())
results = []

def calc(curr, idx, plus, minus, times, div):
    if idx >= n:
        results.append(curr)
    else:
        next = nums[idx]

        if plus > 0:
            calc(curr + next, idx + 1, plus - 1, minus, times, div)
            
        if minus > 0: 
            calc(curr - next, idx + 1, plus, minus - 1, times, div)
            
        if times > 0:
            calc(curr * next, idx + 1, plus, minus, times - 1, div)
            
        if div > 0:
            if curr < 0:
                result = -1 * ((-1 * curr) // next)
            else:
                result = curr // next
            calc(result, idx + 1, plus, minus, times, div - 1)

calc(nums[0], 1, plus, minus, times, div)

print(max(results))
print(min(results))