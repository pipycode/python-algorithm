from collections import deque

N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def bfs(x, y, union, union_num): 
    q = deque([(x, y)])
    union[x][y] = union_num
    population = world[x][y]
    num = 1
    
    while q:
        s = len(q)
        for _ in range(s):
            nowx, nowy = q.popleft()
            for i in range(4):
                nxtx, nxty = nowx + dx[i], nowy + dy[i]
                if 0<=nxtx<N and 0<=nxty<N and not union[nxtx][nxty] and L<=abs(world[nowx][nowy]-world[nxtx][nxty])<=R:
                    union[nxtx][nxty] = union_num
                    population += world[nxtx][nxty]
                    num += 1
                    q.append((nxtx, nxty))
    
    return population // num
            
def move():
    # union : 지도에 각 나라별 union 번호 기록
    # population : 각 union별 population 기록
    union = [[0] * N for _ in range(N)]
    population = [0] * (50 * 50 + 1)
    union_num = 1
    
    # world의 union과 union별 인구수 계산
    for i in range(N):
        for j in range(N):
            if not union[i][j]:
                population[union_num] = bfs(i, j, union, union_num)
                union_num += 1

    # 위의 계산을 토대로 인구이동
    for i in range(N):
        for j in range(N):
            world[i][j] = population[union[i][j]]
    
    if union_num == N * N + 1:
        return False
    else:
        return True

result = 0
while(move()):
    result += 1
print(result)