n, k = map(int, input().split())

# DP[i]는 i를 만드는 방법의 수
DP = [0]*(k+1)
SCORE = [int(input()) for _ in range(n)]
DP[0] = 1
for score in SCORE:
    for i in range(score, k+1):
        DP[i] += DP[i-score]
print(DP[k])
