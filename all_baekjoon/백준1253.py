# Idea
# 1. split: target(좋은수) -> source1 + source2         ?
# 2. merge: source1 + source2 -> target(좋은수)         V 2000C2 = 2백만

from collections import Counter
from itertools import combinations
from bisect import bisect_left, bisect_right

N = int(input())
num = list(map(int, input().split()))
Counter_num = Counter(num)
sorted_num = sorted(Counter_num.keys())
result = {k:False for k in sorted_num}

for x, y in combinations(num, 2):
    # 둘다 0인 경우
    if x==0 and y==0:
        if Counter_num[0] > 2: result[0] = True
    # 0이 하나라도 있는경우
    elif x==0:
        if Counter_num[y] >= 2: result[y] = True
    elif y==0:
        if Counter_num[x] >= 2: result[x] = True
    # 0이 하나도 없는 경우
    else:
        i = bisect_left(sorted_num, x+y)
        if i < len(sorted_num) and sorted_num[i] == x+y:
            result[sorted_num[i]] = True

# 중복값 정리
print(sum([Counter_num[k] for k in result if result[k]]))