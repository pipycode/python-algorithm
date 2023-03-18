# DP[i][0] = i-1과 i를 밟았을 경우 최댓값
# DP[i][1] = i-2와 i를 밟았을 경우 최댓값
# DP[i][0] = DP[i-1][1] + arr[i]
# DP[i][1] = max(DP[i-2][0], DP[i-2][1]) + arr[i]

N = int(input())
SCORE = [0]
SCORE.extend([int(input()) for _ in range(N)])
DP = [[0] * 2 for _ in range(N+1)]

DP[1][0], DP[1][1] = SCORE[1], SCORE[1]
for i in range(2, N+1):
    DP[i][0] = DP[i-1][1] + SCORE[i]
    DP[i][1] = max(DP[i-2][0], DP[i-2][1]) + SCORE[i]

print(max(DP[N]))