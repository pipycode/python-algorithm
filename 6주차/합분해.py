def solution(n):
    N, K = map(int, n.split())
    d = [[0]*(K+1) for _ in range(N+1)] # N과 K 에 따른 합분해 값을 저장하여 값 출력에 사용함

    for i in range(K+1): # 0을 나타내는 경우는 1개 밖에 없음
        d[0][i] = 1

    # K가 3인 경우까지 써보면 겹치는 부분이 있다 = 규칙이 존재
    for i in range(1, N+1):
        for j in range(1, K+1):
            d[i][j] = d[i][j-1] + d[i-1][j] # 규칙(점화식)
            d[i][j] %= 1000000000

    return d[N][K]

n = input()
print(solution(n))