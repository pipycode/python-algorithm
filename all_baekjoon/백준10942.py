N = int(input())
BOARD = list(map(int, input().split()))

dp = [[0] * 2000 for _ in range(2000)]
# dp[i][j] 는 i부터 j까지의 수가 팰린드롬인지 

for d in range(N):
    dp[d][d] = 1
    if d!=(N-1) and BOARD[d] == BOARD[d+1]:
        dp[d][d+1] = 1

# dp[i][j] = if dp[i+1][j-1] and arr[i]==arr[j]: True
for step in range(1, N):
    for diagonal in range(N-step):
        if dp[diagonal+1][step+diagonal-1] and BOARD[diagonal]==BOARD[step+diagonal]:
            dp[diagonal][step+diagonal] = 1

M = int(input())
question = []
for _ in range(M):
    i, j = map(int, input().split())
    question.append((i, j))

for i, j in question:
    print(dp[i-1][j-1])
