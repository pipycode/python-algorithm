from collections import Counter
import re
def solution(s):
    answer = []
    c = Counter()
    for num in re.split(r',|{|}',s):
        if num.isnumeric():
            c[int(num)] += 1
            
    for num in sorted(c.items(), key = lambda x:-x[1]):
        answer.append(num[0])
    return answer