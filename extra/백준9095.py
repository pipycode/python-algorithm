T = int(input())

DP = [0] * 12
DP[1] = 1
DP[2] = 2
DP[3] = 4
for i in range(4, 12):
    DP[i] += (DP[i-1] * DP[1])
    DP[i] += (DP[i-2] * (DP[2] - 1))  # DP[2] = DP[1] + DP[1] -> 위와 겹침
    DP[i] += (DP[i-3] * (DP[3] - 3))  # DP[3] = DP[2] + DP[1] -> 위와 겹침
                                      # DP[3] = DP[1] + DP[1] + DP[1] -> 위와 겹침
                                      # DP[3] = DP[1] + DP[2]
    
for _ in range(T):
    n = int(input())
    print(DP[n])