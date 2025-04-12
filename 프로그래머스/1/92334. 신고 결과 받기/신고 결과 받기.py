def solution(id_list, report, k):
    report_dict = dict()
    mail_dict = dict()
    
    # key: id, value: 해당 id를 신고한 사람 수
    # report의 길이 N -> O(N)
    for r in report:
        reporter, reported = r.split()
        if reported in report_dict:
            report_dict[reported].add(reporter)
        else:
            report_dict[reported] = {reporter}
    
    # key: id, value: 결과 메일을 받은 횟수 
    for key, value in report_dict.items():
        if len(value) >= k:
            for user in value:
                mail_dict[user] = mail_dict.get(user, 0) + 1
    
    result = []
    
    # id_list의 길이 M -> O(M)
    for user in id_list:
        result.append(mail_dict.get(user, 0))
    
    return result