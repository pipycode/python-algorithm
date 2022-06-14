def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles] # puddles 좌표 거꾸로 하기
    roads = [[0] * (m + 1) for i in range(n + 1)]  # 길 초기화
    roads[1][1] = 1 # 시작위치

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles: # 웅덩이 위치의 경우 값을 0으로
                roads[i][j] = 0
            else: # 현재 칸은 왼쪽 칸, 위 칸의 합산
                roads[i][j] = (roads[i - 1][j] + roads[i][j - 1]) % 1000000007
    return roads[n][m]

print(solution(4,3,[[2,2]]))