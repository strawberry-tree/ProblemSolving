from itertools import combinations

def print_cases(nums):
    for cmb in combinations(nums, 6):
        print(*cmb)
    print()
    
while True:
    input_line = list(map(int, input().split()))
    k = input_line[0]
    if k == 0:
        break
    nums = input_line[1:]
    print_cases(nums)