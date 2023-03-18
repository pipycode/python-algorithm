N = int(input())

# 1에서 1을 더하거나 2, 3을 곱해 n만들기
INF = 1e9
DP = [INF] * (N + 1)

DP[1] = 0
for i in range(2, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        DP[i] = min(DP[i-1], DP[i // 2], DP[i // 3]) + 1
    elif i % 2 == 0:
        DP[i] = min(DP[i-1], DP[i // 2]) + 1
    elif i % 3 == 0: 
        DP[i] = min(DP[i-1], DP[i // 3]) + 1
    else:
        DP[i] = DP[i-1] + 1

print(DP[N])