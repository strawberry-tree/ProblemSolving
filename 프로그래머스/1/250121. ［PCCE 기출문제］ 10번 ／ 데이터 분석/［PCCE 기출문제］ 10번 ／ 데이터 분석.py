def solution(data, ext, val_ext, sort_by):
    key_to_code = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    filtered_data = [d for d in data if d[key_to_code[ext]] < val_ext]
    sorted_data = sorted(filtered_data, key=lambda x: x[key_to_code[sort_by]])

    return sorted_data