def solution():
    n = int(input())
    bamboo = []
    for i in range(n):
        bamboo.append(list(map(int,input().split())))
    dp = [ [0] * n ] * n # n x n 개의 리스트
    dpX = [-1, 1, 0, 0]
    dpY = [0, 0, 1, -1]
    answer = 0
    def move(dp, bamX, bamY):
        if dp[bamX][bamY] :
            return dp[bamX][bamY]
        else:
            dp[bamX][bamY] = 1
            for i in range(4):
                movebamX = bamX + dpX[i]
                movebamY = bamY + dpY[i]
                if 0 <= movebamX < n and 0 <= movebamY < n and bamboo[movebamX][movebamY] > bamboo[bamY][bamX] :
                    dp[bamX][bamY] = max(dp[bamX][bamY], move(dp, movebamX, movebamY)+1)
            return dp[bamX][bamY]
    for i in range(n):
        for j in range(n):
            answer = max(answer, move(dp, j, i))
    return answer
print(solution())