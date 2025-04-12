def solution(clothes):
    clothes_dict = dict()
    for _, c_type in clothes:
        clothes_dict[c_type] = clothes_dict.get(c_type, 0) + 1
        
    result = 1
    for c_num in clothes_dict.values():
        result *= (c_num + 1)
    result -= 1
    
    return result
    