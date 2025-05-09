def solution(s):
    s = s[2:-2]
    s_list = [list(map(int, elem.split(","))) for elem in s.split("},{")]
    s_list.sort(key=len)
    
    result = [s_list[0][0]]
    for i in range(1, len(s_list)):
        new_elem = set(s_list[i]) - set(s_list[i-1])
        result.append(list(new_elem)[0])
    return result