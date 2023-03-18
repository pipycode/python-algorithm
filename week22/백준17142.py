N, M = map(int, input().split())

Atlas = [list(map(int, input().split())) for _ in range(N)]
Virus = [(i, j) for i in range(N) for j in range(N) if Atlas[i][j] == 2]

from itertools import combinations
from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
min_time = 51 * 51
init_info = N * N
for i in range(N):
    for j in range(N):
        if Atlas[i][j]:
            init_info -= 1

Virus_C_M = combinations(Virus, M)
for V_list in Virus_C_M:
    # 처음 활성화된 바이러스 위치와 벽의 위치는 Visited = True
    # 맵 전체에 대한 info 저장(info가 0이되면 남는 공간이 없는 것)
    Visited = [[False] * N for _ in range(N)]
    for i, j in V_list:
        Visited[i][j] = True
    info = init_info

    # 전파될 공간이 없을 때까지 반복
    time = 0
    q = deque(V_list)
    while info and q:
        time += 1
        if time >= min_time: break
        q_size = len(q)
        # 모든 바이러스를 현재 전파된 공간에서 빼내어 다음 공간으로 전파
        for _ in range(q_size):
            now = q.popleft()
            for i in range(4):
                nxt_x, nxt_y = now[0] + dx[i], now[1] + dy[i]
                if 0 <= nxt_x < N and 0 <= nxt_y < N and not Visited[nxt_x][nxt_y] and Atlas[nxt_x][nxt_y] != 1:
                    Visited[nxt_x][nxt_y] = True
                    if Atlas[nxt_x][nxt_y] != 2:
                        info -= 1
                    q.append((nxt_x, nxt_y))

    # 모든 빈칸에 바이러스가 있을 경우
    if not info:
        min_time = time
    # 모든 빈칸에 바이러스를 퍼트릴 수 없는 경우는 그냥 패스

if min_time == 51 * 51:
    print(-1)
else:
    print(min_time)

# deepcopy가 시간초과가 난다