
# O(N log N)
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = 0

def two_pointer(i):
    left  = 0
    right = N - 1
    target = nums[i]
    while left < right:
        pointer_sums = nums[left] + nums[right]
        if pointer_sums == target:
            if left != i and right != i:
                return True
            elif left == i:
                left += 1
            else:
                right -= 1
        elif pointer_sums < target:
            left += 1
        else:
            right -= 1
    return False

for i in range(N):
    if two_pointer(i):
        result += 1
print(result)