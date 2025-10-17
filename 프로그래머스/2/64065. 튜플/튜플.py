def solution(s):
    s1 = s[2:-2]    # 맨 처음 {{, }} 없애기
    s1_list = s1.split("},{") # 각 튜플로 나누기 ("a,b,c")꼴
    tuple_list = []
    
    # 2차원 배열로 만들기
    for s1_part in s1_list:
        tuple_list.append(set(map(int, s1_part.split(","))))
    
    # 길이순으로 정렬
    tuple_list.sort(key= lambda x: len(x))
    
    answer = [list(tuple_list[0])[0]]
    
    for i in range(1, len(tuple_list)):
        added = list(tuple_list[i] - tuple_list[i - 1])[0]
        answer.append(added)
    return answer