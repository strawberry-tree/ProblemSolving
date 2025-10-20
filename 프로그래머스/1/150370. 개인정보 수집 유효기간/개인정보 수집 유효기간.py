def solution(today, terms, privacies):
    
    def add_months(d_year, d_month, d_date, add_month):
        add_year = add_month 

        if d_date == 1:
            d_month = d_month + add_month - 1
            d_date = 28
        else:
            d_month += add_month
            d_date -= 1
            
        while d_month > 12:
            d_year += 1
            d_month -= 12
        
        return d_year, d_month, d_date
            
    
    # today, terms 값 구성
    t_year, t_month, t_date = map(int, today.split("."))
    terms_dict = dict()
    for term in terms:
        key, value = term.split(" ")
        terms_dict[key] = int(value)
    
    result = []
    # 각 privacy 순회
    for i, privacy in enumerate(privacies):
        date, term_key = privacy.split()
        d_year, d_month, d_date = map(int, date.split("."))
        r_year, r_month, r_date = add_months(d_year, d_month, d_date, terms_dict[term_key])

        flag1 = r_year < t_year
        flag2 = r_year == t_year and r_month < t_month
        flag3 = r_year == t_year and r_month == t_month and r_date < t_date
        
        if flag1 or flag2 or flag3:
            result.append(i + 1)
            
    return result