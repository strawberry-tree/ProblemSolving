def solution(record):
    user_dict = dict()  # id - 닉네임
    history = []        # 입퇴장 기록
    
    # O(N) - 유저 아이디와 닉네임 / 입퇴장 기록 저장
    for r in record:
        command, userdata = r.split(" ", 1)
        if command == "Enter":
            userid, nickname = userdata.split()
            user_dict[userid] = nickname
            history.append((userid, "enter"))
        elif command == "Leave":
            history.append((userdata, "leave"))            
        elif command == "Change":
            userid, nickname = userdata.split()
            user_dict[userid] = nickname
    
    # O(N) - result 배열 반들기
    result = []
    
    for userid, command in history:
        if command == "enter":
            result.append(f"{user_dict[userid]}님이 들어왔습니다.")
        elif command == "leave":
            result.append(f"{user_dict[userid]}님이 나갔습니다.")
    
    return result
            