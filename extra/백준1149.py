N = int(input())
INF = 1e9
DP = [[INF] * 3 for _ in range(N)]

# DP[i][0] = i번째 집이 R일때 최솟값
# DP[i][1] = i번째 집이 G일때 최솟값
# DP[i][2] = i번째 집이 B일때 최솟값
DP[0] = list(map(int, input().split()))
for i in range(1, N):
    COST = list(map(int, input().split()))
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + COST[0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + COST[1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + COST[2]
    
print(min(DP[N-1]))