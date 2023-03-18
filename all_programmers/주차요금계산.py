import math
from collections import Counter
def solution(fees, records):
    answer = []
    total = dict()
    for record in records:
        time = (int(record[:2]) * 60) + int(record[3:5])
        name = record[6:10]
        info = record[11:]
        # total[x] = [누적시간, 마지막 시간 기록, info]
        if name in total:
            if info == "OUT":
                total[name][0] += (time - total[name][1])
                total[name][1] = time
                total[name][2] = "OUT"
            else:
                total[name][1] = time
                total[name][2] = "IN"
        else:
            total[name] = [0, time, info]
    for name in total:
        if total[name][2] == "IN":
            total[name][0] += ((23*60 + 59) - total[name][1])
            
    for data in sorted(total):
        time = total[data][0]
        fee = fees[1]
        if fees[0] < time:
            fee += (math.ceil((time - fees[0]) / fees[2]) * fees[3])
        answer.append(fee)
    return answer