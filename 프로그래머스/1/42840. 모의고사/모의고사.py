def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(answers)):
        correct_answer = answers[i]
        answer_1 = student_1[i % len(student_1)]
        if correct_answer == answer_1:
            scores[1] += 1
        
        answer_2 = student_2[i % len(student_2)]
        if correct_answer == answer_2:
            scores[2] += 1
        
        answer_3 = student_3[i % len(student_3)]
        if correct_answer == answer_3:
            scores[3] += 1
        
    max_score = max(scores.values())
    
    answer = []
    
    for i in range(1, 4):
        if scores[i] == max_score:
            answer.append(i)
            
    return answer