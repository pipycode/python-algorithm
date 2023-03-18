def solution(money):
    if len(money) == 3:
        return max(money)
    # DP[i] 는 i번 집을 털었을 때, 가질 수 있는 최댓값
    # 마지막 두 집의 연속성을 없애기 위해
    # 1. 마지막 집을 털었을 경우 : 2 ~ n-2 의 최댓값 + n
    DP1 = [0] * len(money)
    DP1[1], DP1[2], DP1[3] = money[1], money[2], money[1] + money[3]
    
    # 2. 마지막 집을 털지 않았을 경우 : 1 ~ n-1 의 최댓값
    DP2 = [0] * len(money)
    DP2[0], DP2[1], DP2[2] = money[0], money[1], money[0] + money[2]
    
    for i in range(len(money)):
        if i >= 4 and i < len(money) - 2:
            if DP1[i - 3] + money[i] > DP1[i - 2] + money[i]:
                DP1[i] = DP1[i - 3] + money[i]
            else:
                DP1[i] = DP1[i - 2] + money[i]
        
        if i >= 3 and i < len(money) - 1:
            if DP2[i - 3] + money[i] > DP2[i - 2] + money[i]:
                DP2[i] = DP2[i - 3] + money[i]
            else:
                DP2[i] = DP2[i - 2] + money[i]
    
    one = max(DP1)
    two = max(DP2)
    
    answer = max(one + money[len(DP1) - 1], two)
    
    return answer

# 1 2 3 1 3 4 5 1 2 3 6   1 2 3 1 3 4 5 1 2 3 6