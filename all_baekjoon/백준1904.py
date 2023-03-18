N = int(input())

DP = [[0] * 2 for _ in range(N+1)]
DP[1][0], DP[1][1] = 0, 1
if N > 1:
    DP[2][0], DP[2][1] = 1, 1
for i in range(3, N+1):
    DP[i][0] = (DP[i-2][0] % 15746 + DP[i-2][1] % 15746)
    DP[i][1] = (DP[i-1][0] % 15746 + DP[i-1][1] % 15746)
    
print(sum(DP[N]) % 15746)