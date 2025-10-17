def solution(phone_book):
    phone_set = set(phone_book)
    
    for p in phone_book:
        for k in range(min(20, len(p))):
            if p[:k] in phone_set:
                return False
    return True