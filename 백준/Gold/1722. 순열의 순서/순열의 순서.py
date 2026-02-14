N = int(input())
cases = [1]                                 # [1, 2, 6]
order = [i for i in range(1, N + 1)]        # [1, 2, 3, 4]

for i in range(2, N):
    cases.append(cases[-1] * i)

def get_kth_perm(k):
    k = k - 1
    while len(order) > 1:
        mok, nam = divmod(k, cases.pop())
        print(order[mok], end = " ")
        order.remove(order[mok])
        k = nam
    print(order[0])
    
    
def get_perm_order(perm):
    result = 1
    for p in perm[:-1]:
        result += cases.pop() * order.index(p)
        order.remove(p)
    return result
    
nums = list(map(int, input().split()))

if nums[0] == 1:
    get_kth_perm(nums[1])
elif nums[0] == 2:
    print(get_perm_order(nums[1:]))