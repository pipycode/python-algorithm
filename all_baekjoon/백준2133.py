# Idea
# 1. Wall[i][j] 는 i, j에 타일의 꼭짓점(오른쪽 아래)이 존재하는 경우의 수
# --> Wall[0][j] = Wall[i][j] ....???
# 2. Wall[i]는 3xi의 벽을 채우는 경우의 수

N = int(input())
Wall = [0] * (30 + 1)

Wall[1] = 0
Wall[2] = 3
for i in range(3, N+1):
    # 홀수이면 벽을 채우는 경우의 수가 존재하지 않음
    if i%2 == 1:
        Wall[i] = 0
    # Wall[i] = 2 + (Wall[i-2] * 3) + (Wall[i-4] * 2) + ... (Wall[2] * 2)
    else:
        for j in range(2, i - 2 + 1):
            Wall[i] += (Wall[i-j] * 2)
        Wall[i] += (2 + Wall[i-2])     
print(Wall[N])