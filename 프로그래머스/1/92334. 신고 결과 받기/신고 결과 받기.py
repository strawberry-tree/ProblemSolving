# 
# report: [신고한id 신고당한id]

from collections import defaultdict

def solution(id_list, report, k):
    # 딕셔너리 만들기 - {신고당한id: [신고한id의 set]}
    report_dict = defaultdict(set)
    for r in report:
        reporter, reported = r.split()
        report_dict[reported].add(reporter)
    
    # 신고횟수 세기 - {id: 받은 이메일 수}
    email_dict = defaultdict(int)
    
    for key, value in report_dict.items():
        # k회 이상 신고당하면 정지
        if len(value) >= k:
            # 신고당한 사용자는 메일을 받지
            for user in value:
                email_dict[user] += 1
                
    # 정답 반환
    answer = []
    for user_id in id_list:
        answer.append(email_dict[user_id])
    return answer    