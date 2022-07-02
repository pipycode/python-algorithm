def solution(money):
    N = money
    dp = [ [0 for i in N] for j in N]
    
    for i in range(len(N)):
        j = 0
        M = (N+N)[i:i+len(N)]
        print(M)
        while(True):
            if j >= len(N)-1:
                break
            if j == 0:
                dp[i][j] = dp[i][j]+M[j]
                j += 2
            elif j+1 == len(N)-1:
                dp[i][j] = dp[i][j]+M[j]
                j += 2
            elif dp[i][j] +M[j] >= dp[i][j] + M[j+1]:
                dp[i][j] = max(dp[i][j] +M[j] , dp[i][j] + M[j+1])
                j += 2
            else:
                j += 1
    answer = max(map(sum,dp))
    return answer

print(solution([1,1,1,1,1]))