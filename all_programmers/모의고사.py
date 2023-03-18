def solution(answers):
    answer = []
    l = len(answers)
    one = [1, 2, 3, 4, 5] * (int(l/5) + 1)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (int(l/8) + 1)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (int(l/10) + 1)
    result = [0, 0, 0]
    for i, ans in enumerate(answers):
        if one[i] == ans: result[0] += 1
        if two[i] == ans: result[1] += 1 
        if three[i] == ans: result[2] += 1
    m = max(result)
    for i, d in enumerate(result):
        if d == m: answer.append(i+1)
    return answer