def solution(array, commands):
    answer=[]
    for i, j, k in commands:
        sliced_array = array[i-1:j]
        sliced_array.sort()
        answer.append(sliced_array[k - 1])
    return answer