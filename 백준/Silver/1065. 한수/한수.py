N = int(input())

def check_hansu(num):
    num_str = str(num)
    if len(num_str) <= 2:
        return True
    change = int(num_str[1]) - int(num_str[0])
    
    for i in range(2, len(num_str)):
        if (int(num_str[i]) - int(num_str[i - 1])) != change:
            return False
    return True

answer = sum(check_hansu(num) for num in range(1, N + 1))
print(answer)