import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    std_day = 0
    for p, s in zip(progresses, speeds):
        remain_day = math.ceil((100-p) / s)
        if std_day >= remain_day:
            answer[len(answer)-1] += 1
        else:
            answer.append(1)
            std_day = remain_day
        
    return answer