# N = []
# while(1):
#     put = int(input())
#     if put == 0:
#         break
#     N.append(put)
# for n in N:
#     dp = [['']] * n
#     if n == 1:
#         print(1)
#     else:
#         for i in range(n):
#             if i == 0:
#                 dp[0] = ['WH']
#                 SUM = []
#             else:
#                 for word in dp[i-1]:
#                     SUM += (list(set([word+'WH', 'W'+word+'H', 'WH'+word])))
#                 dp[i] = SUM
#                 SUM = []
#         print(len(dp[n-1]))
N = []
dp = [ [0 for i in range(31)] for j in range(31)]
for i in range(31):
    dp[0][i] = 1
for i in range(31):
    for j in range(i,31):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
while(1):
    put = int(input())
    if put == 0:
        break
    N.append(put)
for n in N:
    print(dp[n][n])
    
