def solution(video_len, pos, op_start, op_end, commands):
    # 분, 초 구하기
    video_mm, video_ss = map(int, video_len.split(":"))
    video_time = video_mm * 60 + video_ss
    pos_mm, pos_ss = map(int, pos.split(":"))
    pos_time = pos_mm * 60 + pos_ss
    op_start_mm, op_start_ss = map(int, op_start.split(":"))
    op_start_time = op_start_mm * 60 + op_start_ss
    op_end_mm, op_end_ss = map(int, op_end.split(":"))
    op_end_time = op_end_mm * 60 + op_end_ss
    
    
    for c in commands:
        if op_start_time <= pos_time < op_end_time:
            pos_time = op_end_time 
        if c == "prev":
            pos_time = max(0, pos_time - 10)
        elif c == "next":        
            pos_time = min(pos_time + 10, video_time)
            
    if op_start_time <= pos_time < op_end_time:
        pos_time = op_end_time 
            
    final_mm = pos_time // 60
    final_ss = pos_time % 60
    result = f"{final_mm:0>2}:{final_ss:0>2}"
    
    return result