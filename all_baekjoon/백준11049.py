N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

DP = [[0] * 500 for _ in range(500)]

for i in range(1, N):
    for j in range(0, N-i):
        DP[j][i+j] = 1e11
        for k in range(j, j+i):
            DP[j][i+j] = min(DP[j][k] + DP[k+1][i+j] + matrix[j][0]*matrix[k][1]*matrix[i+j][1],
                             DP[j][i+j])
print(DP[0][N-1])